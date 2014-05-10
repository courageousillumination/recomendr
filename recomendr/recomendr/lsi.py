from recomendr.recomendr.models import Course
from gensim import corpora, models, similarities
import string
import heapq

DICTIONARY = None
LSI = None
INDEX = None

def process_string(s):
    remove_punctuation_map = dict((ord(char), ord(' ')) for char in string.punctuation)
    return [word.translate(remove_punctuation_map).strip() for word in s.lower().split()]

def save_index(prefix, index):
    index.save(prefix + "courses.index")
    
def load_lsi(prefix):
    dictionary = corpora.Dictionary.load_from_text(prefix + "wikipedia_wordids.txt")
    lsi = models.lsimodel.LsiModel.load(prefix + "topic_model.lsi")
    return dictionary, lsi
    
def load_index(prefix):
    index = similarities.MatrixSimilarity.load(prefix + "courses.index")
    return index

def get_similar(document, dictionary, lda, index):
    vec = lda[dictionary.doc2bow(process_string(document))]
    sims = index[vec]
    return [(x, y) for x, y in list(enumerate(sims)) if y != 1.0]

def get_similar_courses(course, num_courses):
    r = get_similar(course.title + ' ' + course.description, DICTIONARY, LSI, INDEX)
    return Course.objects.filter(id__in = [x[0] for x in heapq.nlargest(num_courses, r, key= lambda x: x[1])])

def get_similar_courses_list(courses, num_similar):
    course_ids = set(x.id for x in courses)
    x = [DICTIONARY.doc2bow(process_string(course.title + ' ' + course.description)) for course in courses]
    sim = INDEX[LSI[x]]
    summed = sim[0]
    for i in range(1, len(sim)):
        summed += sim[i]
    sim = [(x, y) for x, y in list(enumerate(summed)) if x not in course_ids]
    return Course.objects.filter(id__in = [x[0] for x in heapq.nlargest(num_similar, sim, key= lambda x: x[1])])

#Upon importing this we check to see if the files exist. If they
#don't we have to create them
DICTIONARY, LSI = load_lsi("data/")
try:
    INDEX = load_index("data/")
except IOError:
    documents = []
    for course in Course.objects.all():
        documents.append(course.title + ' ' + course.description)
    print "Couldn't find similarity matrix, rebuilding... (this could take a while)"
    documents = [DICTIONARY.doc2bow(process_string(x)) for x in documents]
    INDEX = similarities.MatrixSimilarity(LSI[documents], num_features=100000)
    save_index("data/", INDEX)
