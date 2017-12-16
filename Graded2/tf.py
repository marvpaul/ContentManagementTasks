from os import listdir
from os.path import isfile, join
import re

def prepare_text(text):
    '''
    Prepare a given text. Remove stopwords, punctation and other stuff
    :param text: a text
    :return: array with remaining words in text
    '''
    #Remove html tags
    text = re.sub('<[^>]*>', '', text)
    #Remove line breaks
    text = re.sub('\n', ' ', text)

    unimportant_stuff = ['.', ',']
    for char in unimportant_stuff:
        text = re.sub('[' + char + ']', '', text)

    #remove doubled whitespaces
    text = re.sub(' +', ' ', text)

    #remove stop words
    stop_words = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08',
                  'a', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do',
                  'for', 'have', 'is', 'in', 'it', 'of', 'or', 'see', 'so',
                  'that', 'the', 'this', 'to', 'we']
    text = str.lower(text)
    for stop_word in stop_words:
        text = re.sub(' ' + stop_word + '[. ]', ' ', text)

    #Make array of words
    text = text.split(" ")

    #filter whitespaces
    text = list(filter(None, text))

    return text

def count_words(text):
    '''
    Count words in text
    :param text: array with words to count
    :return: a dic with word -> count
    '''
    dic = {}
    for word in text:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

files = [f for f in listdir("tutorial/") if isfile(join("tutorial/", f))]
scraped_files = []

for file in files:
    if "html" in file:
        scraped_files.append(file)

output = ""
for file in scraped_files:
    f = open("tutorial/" + file, 'r+')
    file_content = (f.readlines())
    file_content = ''.join(file_content)
    file_content = prepare_text(file_content)
    print("{", file, ": ", count_words(file_content), "}")
    output += "{\"" + file + "\" : " + str(count_words(file_content)).replace("\'", "\"") + "}\n"

with open('index.txt', 'a') as the_file:
    the_file.write(output)