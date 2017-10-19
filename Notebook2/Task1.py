import re

def analyseText(text):
    text = re.sub('[\W]', " ", text)

    text = re.sub('[\S]]', "", text)

    char_occurences = {}

    #Case unsensitive
    text = text.lower()

    #remove all spaces
    text = re.sub(" {1, }", "", text)

    #remove all umlaute
    umlaute = {"ä" : "ae", "ö": "oe", "ü" : "ue", "³":"", "à":""}
    for k in umlaute:
        text = re.sub(k, umlaute[k], text)



    #remove all special chars
    text = re.sub("[\d]", "", text)

    for char in list(text):
        if(char in char_occurences):
            char_occurences[char] += 1
        else:
            char_occurences[char] = 1
    return char_occurences


def getMatchScore(char_occurences, mostFreqCharInLang, leastFreqCharInLang):
    #sort
    order = sorted(char_occurences, key= lambda k: char_occurences[k])

    #result
    mostFreqUsedInText = order[len(order)-6:len(order)]
    leastFreqUsedInText = order[0:6]
    score = 0
    for char in mostFreqUsedInText:
        if char in mostFreqCharInLang:
            score += 1

    for char in leastFreqUsedInText:
        if char in leastFreqCharInLang:
            score += 1
    return score

text1 = ""
with open('text1.txt', 'r') as f:
    text1 = f.read()

text2 = ""
with open('text2.txt', 'r') as f:
    text2 += f.read()


mostFrequentGerChars = ['e', 'n', 'i', 's', 'r', 'a']
leastFrequentGerChars = ['v', 'ß', 'j', 'y', 'x', 'q']

mostFrequentEngChars = ['e', 't', 'a', 'o', 'i', 'n']
leastFrequentEngChars = ['z', 'q', 'x', 'j', 'k', 'v']

print("Freq match score text1")
print("Ger:" + str(getMatchScore(analyseText(text1), mostFrequentGerChars, leastFrequentGerChars)))
print("Eng:" + str(getMatchScore(analyseText(text1), mostFrequentEngChars, leastFrequentEngChars)))


print("Freq match score text2")
print("Ger:" + str(getMatchScore(analyseText(text2), mostFrequentGerChars, leastFrequentGerChars)))
print("Eng:" + str(getMatchScore(analyseText(text2), mostFrequentEngChars, leastFrequentEngChars)))