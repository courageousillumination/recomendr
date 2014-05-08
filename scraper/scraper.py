import lxml.html
import re
import requests
import pickle

base_url = "http://collegecatalog.uchicago.edu"

links = """
<li><a href="/thecollege/anthropology/">Anthropology</a></li>
<li><a href="/thecollege/arthistory/">Art History</a></li>
<li><a href="/thecollege/biologicalchemistry/">Biological Chemistry</a></li>
<li><a href="/thecollege/biologicalsciences/">Biological Sciences</a></li>
<li><a href="/thecollege/chemistry/">Chemistry</a></li>
<li><a href="/thecollege/cinemamediastudies/">Cinema and Media Studies</a></li>
<li><a href="/thecollege/civilizationstudies/">Civilization Studies</a></li>
<li><a href="/thecollege/classicalstudies/">Classical Studies</a></li>
<li><a href="/thecollege/comparativehumandevelopment/">Comparative Human Development</a></li>
<li><a href="/thecollege/comparativeliterature/">Comparative Literature</a></li>
<li><a href="/thecollege/comparativeraceethnicstudies/">Comparative Race and Ethnic Studies</a></li>
<li><a href="/thecollege/computerscience/">Computer Science</a></li>
<li><a href="/thecollege/eastasianlanguagescivilizations/">East Asian Languages and Civilizations</a></li>
<li><a href="/thecollege/economics/">Economics</a></li>
<li><a href="/thecollege/englishlanguageliterature/">English Language and Literature</a></li>
<li><a href="/thecollege/environmentalscience/">Environmental Science</a></li>
<li><a href="/thecollege/environmentalstudies/">Environmental Studies</a></li>
<li><a href="/thecollege/fundamentalsissuesandtexts/">Fundamentals: Issues and Texts</a></li>
<li><a href="/thecollege/genderstudies/">Gender and Sexuality Studies</a></li>
<li><a href="/thecollege/geographicalstudies/">Geographical Studies</a></li>
<li><a href="/thecollege/geophysicalsciences/">Geophysical Sciences</a></li>
<li><a href="/thecollege/germanicstudies/">Germanic Studies</a></li>
<li><a href="/thecollege/history/">History</a></li>
<li><a href="/thecollege/scienceandmedicinehips/">History, Philosophy, and Social Studies of Science and Medicine</a></li>
<li><a href="/thecollege/humanities/">Humanities</a></li>
<li><a href="/thecollege/interdisciplinarystudieshumanities/">Interdisciplinary Studies in the Humanities</a></li>
<li><a href="/thecollege/internationalstudies/">International Studies</a></li>
<li><a href="/thecollege/jewishstudies/">Jewish Studies</a></li>
<li><a href="/thecollege/latinamericanstudies/">Latin American Studies</a></li>
<li><a href="/thecollege/lawlettersandsociety/">Law, Letters, and Society</a></li>
<li><a href="/thecollege/linguistics/">Linguistics</a></li>
<li><a href="/thecollege/mathematics/">Mathematics</a></li>
<li><a href="/thecollege/medievalstudies/">Medieval Studies</a></li>
<li><a href="/thecollege/music/">Music</a></li>
<li><a href="/thecollege/naturalsciences/">Natural Sciences</a></li>
<li><a href="/thecollege/neareasternlanguagescivilizations/">Near Eastern Languages and Civilizations</a></li>
<li><a href="/thecollege/newcollegiatedivision/">New Collegiate Division</a></li>
<li><a href="/thecollege/philosophy/">Philosophy</a></li>
<li><a href="/thecollege/physicalsciences/">Physical Sciences</a></li>
<li><a href="/thecollege/physics/">Physics</a></li>
<li><a href="/thecollege/politicalscience/">Political Science</a></li>
<li><a href="/thecollege/psychology/">Psychology</a></li>
<li><a href="/thecollege/publicpolicystudies/">Public Policy Studies</a></li>
<li><a href="/thecollege/religiousstudies/">Religious Studies</a></li>
<li><a href="/thecollege/romancelanguagesliteratures/">Romance Languages and Literatures</a></li>
<li><a href="/thecollege/russianstudies/">Russian Studies</a></li>
<li><a href="/thecollege/slaviclanguagesliteratures/">Slavic Languages and Literatures</a></li>
<li><a href="/thecollege/socialsciences/">Social Sciences</a></li>
<li><a href="/thecollege/sociology/">Sociology</a></li>
<li><a href="/thecollege/southasianlanguagescivilizations/">South Asian Languages and Civilizations</a></li>
<li><a href="/thecollege/statistics/">Statistics</a></li>
<li><a href="/thecollege/theaterperformancestudies/">Theater and Performance Studies</a></li>
<li><a href="/thecollege/tutorialstudies/">Tutorial Studies</a></li>
<li><a href="/thecollege/visualarts/">Visual Arts</a></li>
"""

urls = [base_url + x for x in re.findall('(?<=<li><a href=").+(?=")', links)]
html = []
for x in urls:
    html.append(requests.get(x).text)
    print "Got {0}".format(x)
print "Got all the webpages."

all_classes = []
for doc in html:
    tree = lxml.html.fromstring(doc)

    elements = list(tree.find_class("courseblock"))

    for i in range(len(elements)):
        element = elements[i]
        
        #No sequences
        if i < len(elements) - 1 and "subsequence" in elements[i+1].values()[0]:
            continue
        #Extract the title information
        
        title = element.find_class("courseblocktitle")[0].getchildren()[0].text
        a = title.split('.')
        identifier = a[0].strip()
        name = a[1].strip()
        
        #Extract the description
        description = element.find_class("courseblockdesc")[0].text
        
        all_classes.append({"name": name, "id": identifier, "description":description})
        
        
pickle.dump(all_classes, open("all_classes.p", "wb"))