import csv
import Graded1.DecisionTree as tree
import numpy as np

def readData(path):
    data = []
    header = ""
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        header = next(reader)
        data = []
        for row in reader:
            data.append(row)
    return header, data

def createDic(header, data):
    dic = {}
    new_data = []
    for entry in data:
        for value_number in range(len(entry)):
            dic[header[value_number]] = entry[value_number]
        new_data.append(dic)
        dic = {}
    return new_data


def deleteUnimportantData(data, unimportantData):
    for entry in data:
        for key in unimportantData:
            del entry[key]
    return data

def addFamilySizeFeature(data):
    for entry in data:
        entry['Family_size'] = int(entry['SibSp']) + int(entry['Parch'])
    return data

def categorizeAge(data):
    categoriez = {
        "child" : [0, 14],
        "adult" : [15, 50],
        "old" : [51, 100]
    }
    for entry in data:
        if entry['Age'] == "":
            entry['Age'] = "0"
        elif float(entry['Age']) <= 18:
            entry['Age'] = "1"
        elif float(entry['Age']) <= 55:
            entry['Age'] = "2"
        else:
            entry['Age'] = "3"
    return data

header, data = readData("train.csv")

data = createDic(header, data)
data = addFamilySizeFeature(data)
simplifiedData = deleteUnimportantData(data, ["Name", "Ticket", "Fare", "Cabin", "Embarked", "Parch", "SibSp"])
simplifiedData = categorizeAge(simplifiedData)
print(simplifiedData)

features = ['Pclass', 'Sex', 'Age', 'Family_size']
tree1 = tree.Tree()
tree1.getTree(simplifiedData, features)
survived = tree1.evealuteData(data)


actualSurvived = []
for entry in data:
    actualSurvived.append(int(entry['Survived']))

counter = 0
for i in range(len(survived)):
    if survived[i] == actualSurvived[i]:
        counter += 1

print(counter / len(data))


#p = tree1.computeProps(simplifiedData)
#entireEntropy = tree1.computeEntropy(p)
#print("Entropy", entireEntropy)
props = tree1.getPropRec(simplifiedData, ['Sex', 'Family_size', 'Age'])



#print("Entropy splitted by Sex: ", tree.computeEntropy(props))
