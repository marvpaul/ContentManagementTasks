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
    for entry in data:
        if entry['Age'] == "":
            entry['Age'] = "0"
        elif float(entry['Age']) <= 16:
            entry['Age'] = "1"
        elif float(entry['Age']) <= 35:
            entry['Age'] = "2"
        elif float(entry['Age']) <= 50:
            entry['Age'] = "3"
        else:
            entry['Age'] = "4"
    return data

def categorizeCabin(data):
    for entry in data:
        if "A" in entry['Cabin'] or "B" in entry['Cabin'] or "C" in entry['Cabin']:
            entry['Cabin'] = 1
        elif "D" in entry['Cabin'] or "E" in entry['Cabin']:
            entry['Cabin'] = 2
        else:
            entry['Cabin'] = 3
    return data

def prepareData(path):
    header, data = readData(path)
    data = createDic(header, data)
    data = addFamilySizeFeature(data)
    simplifiedData = deleteUnimportantData(data, ["Name", "Ticket", "Fare", "Parch", "SibSp"])
    simplifiedData = categorizeAge(simplifiedData)
    simplifiedData = categorizeCabin(simplifiedData)
    return simplifiedData


data = prepareData("train.csv")

#Features to use for decision tree
features = ['Pclass', 'Sex', 'Age', 'Family_size']# 'Cabin'®

#Create a tree with given trainingsdata and selected features
tree1 = tree.Tree()
tree1.getTree(data, features)

#First evaluation
survived = tree1.evealuteData(data)

#Load and evaluate test data o.o
testData = prepareData("test.csv")
survivedTest = tree1.evealuteData(testData)

header, dataset = readData("test_validation.csv")
real_data = createDic(header, dataset)

real_survived = []
for entry in real_data:
    real_survived.append(int(entry['Survived']))
counter = 0
for i in range(len(survivedTest)):
    if survivedTest[i] == real_survived[i]:
        counter += 1

print(counter / len(testData), " accuracy. Whats going on here? :S")

actualSurvived = []
for entry in data:
    actualSurvived.append(int(entry['Survived']))

counter = 0
for i in range(len(survived)):
    if survived[i] == actualSurvived[i]:
        counter += 1

print(counter / len(data))
