import itertools
import string

with open('encrypt.txt', 'r') as f:
    line = f.read()
my_list = line.split(",")

def decryptWithPass(password, text):
    counter = 0
    decryptedText = ""
    for char in text:
        decryptedText += chr(ord(password[counter]) ^ int(char))
        counter += 1
        if counter == len(password):
            counter = 0
    return decryptedText

def wordScore(words, text):
    score = 0
    for word in words:
        score += text.count(" " + word + " ")
    return score

print(decryptWithPass('god', my_list))

mostCommonEngWords = ['the', 'to', 'be', 'of', 'and', 'a', 'in', 'that']
allPasses = [''.join(i) for i in itertools.product(list(string.ascii_lowercase), repeat=3)]

possiblePasses = [[]]
for passwordSample in allPasses:
    score = wordScore(mostCommonEngWords, decryptWithPass(passwordSample, my_list))
    if(score > 0):
        possiblePasses.append([score, passwordSample])
        possiblePasses = sorted(possiblePasses, key= lambda k : k)

print(possiblePasses[len(possiblePasses)-1])

