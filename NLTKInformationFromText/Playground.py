import nltk

'''document = "This is my super awesome sentence! Just leave the house and close the door."

#Split into sentences
sentences = nltk.sent_tokenize(document)
print(sentences)

#Split into words and punctuation --> http://www.nltk.org/_modules/nltk/tokenize.html
tokenized = [nltk.word_tokenize(sent) for sent in sentences]
print(tokenized)

#Part of speech tagging / Wortarten
#Explanation
#DT --> Artikel
#JJ --> Adjektiv
#NN --> Noun
speed_tags = [nltk.pos_tag(sent) for sent in tokenized]

#structured data
orgs = [("Omnicom", "New York"), ("DDB Needham", "New York"), ("Kaplan Thaler Group", "New York"), ("BBDO South", "Atlanta"), ("Georgia-Pacific", "Atlanta")]

#Orgs in Atlanta?
for org in orgs:
    if org[1] == "Atlanta":
        print(org[0], " is in Atlanta")

#Unstructured data
orgs_sentences = "The fourth Wells account moving to another agency is the packaged paper- " \
                 "products division of Georgia-Pacific Corp., which arrived at Wells only last fall." \
                 " Like Hertz and the History Channel, it is also leaving for an Omnicom-owned agency, " \
                 "the BBDO South unit of BBDO Worldwide. BBDO South in Atlanta, which handles corporate " \
                 "advertising for Georgia-Pacific, will assume additional duties for brands like Angel Soft " \
                 "toilet tissue and Sparkle paper towels, said Ken Haldin, a spokesman for Georgia-Pacific in Atlanta."
'''
#--> Trying to do information extraction --> Creating structured data from text to determine the copanies location
#Showing image of information extraction architecture


#Entity recognition
#--> Segmentation and labeling of entities which are in a potential relation

#Chunking
#Select a subset of tokens, f.e. the yellow dog

#NP Chunking
#Chunks with a noun

#Simple chunk grammar with a tag pattern regex
'''sentence = "The little yellow dog barked at the cat."
tokenized = [nltk.word_tokenize(sentence)]
speed_tags = [nltk.pos_tag(token) for token in tokenized]
print(speed_tags)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(speed_tags[0])
print(result)
result.draw()'''


doc = nltk.corpus.ieer.parsed_docs('NYT_19980315')
for text in doc:
    print(text.text)


sentence = "his Mansion House speech the price cutting CD to CD more than the fastest developing trends skill."
tokenized = [nltk.word_tokenize(sentence)]
speed_tags = [nltk.pos_tag(token) for token in tokenized]
print(speed_tags)