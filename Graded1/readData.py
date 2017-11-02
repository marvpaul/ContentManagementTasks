import csv
import Graded1.DecisionTree as tree

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

header, data = readData("train.csv")

data = createDic(header, data)
data = addFamilySizeFeature(data)
simplifiedData = deleteUnimportantData(data, ["Name", "Ticket", "Fare", "Cabin", "Embarked", "Parch", "SibSp"])
print(simplifiedData)

p = tree.computeProps(data)
entireEntropy = tree.computeEntropy(p)
print(entireEntropy)
print(tree.computeEntropy([1, 0]))