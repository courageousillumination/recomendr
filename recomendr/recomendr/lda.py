from recomendr.recomendr.models import Course
from gensim import corpora, models, similarities
import string
import heapq

DICTIONARY = None
LDA = None
INDEX = None

def process_string(s):
    remove_punctuation_map = dict((ord(char), ord(' ')) for char in string.punctuation)
    return [word.translate(remove_punctuation_map).strip() for word in s.lower().split()]

def generate_tokens(texts):
    all_tokens = sum(texts, [])
    tokens = { }
    for word in all_tokens:
        try:
            tokens[word] += 1
        except KeyError:
            tokens[word] = 1
    tokens = tokens.items()
    tokens.sort(key = lambda x: x[1], reverse = True)
    tokens = tokens[30:]#Just drop the 30 most common words
    tokens_once = set(x for x, y in tokens if y != 1) 
    return tokens_once

def create_dictionary(documents):
    texts = [process_string(document) for document in documents]
    tokens = generate_tokens(texts)
    result = [[word for word in text if word in tokens] for text in texts]
    return result

def create_lda(documents):
    texts = create_dictionary(documents)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, update_every=0, passes=20)
    index = similarities.MatrixSimilarity(lda[corpus])
    
    return dictionary, corpus, lda, index

def save_lda(prefix, dictionary, lda, index):
    dictionary.save(prefix + ".dict")
    lda.save(prefix + ".lda")
    index.save(prefix + ".index")
    
def load_lda(prefix):
    dictionary = corpora.Dictionary.load(prefix + ".dict")
    lda = models.ldamodel.LdaModel.load(prefix + ".lda")
    index = similarities.MatrixSimilarity.load(prefix + ".index")
    
    return dictionary, lda, index

def get_similar(document, dictionary, lda, index):
    vec = lda[dictionary.doc2bow(process_string(document))]
    sims = index[vec]
    #result = list(enumerate(sims))
    #result.sort(key = lambda x: x[1], reverse = True)
    return [(x, y) for x, y in list(enumerate(sims)) if y != 1.0]

def get_similar_courses(course, num_courses):
    r = get_similar(course.description, DICTIONARY, LDA, INDEX)
    return Course.objects.filter(id__in = [x[0] for x in heapq.nlargest(num_courses, r, key= lambda x: x[1]) if x[1] > 0.7])

#Upon importing this we check to see if the files exist. If they
#don't we have to create them
try:
    DICTIONARY, LDA, INDEX = load_lda("data/courses")
except IOError:
    documents = []
    for course in Course.objects.all():
        documents.append(course.description)
    print "Couldn't find similarity matrix, rebuilding... (this could take a while)"
    DICTIONARY, CORPUS, LDA, INDEX = create_lda(documents)
    save_lda("data/courses", DICTIONARY, LDA, INDEX)
