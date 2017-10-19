def getScore(name, position):
    "this function calculates the score for a name depending on chars and the position in a name list"
    score = 0
    for char in list(name):
        score += ord(char) - ord('A') + 1
    return score

def readAndProcessNamelist(path):
    "This function reads and process a given name list located at path"
    with open(path, 'r') as f:
        line = f.read()
    line = line.replace('\"', '')
    nameArray = line.split(',')
    nameArray.sort()
    return nameArray


#Euler 22

nameArray = readAndProcessNamelist('p022_names.txt')
score = 0

#Iterate through all the names in the given name list
for idx, name in enumerate(nameArray):
    score += getScore(name, idx+1) * (idx+1)
#Here we go, print it out!
print(score)