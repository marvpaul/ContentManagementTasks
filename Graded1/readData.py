import Graded1.dataProcessingHelper as dp
import Graded1.FeatureEngeneeringHelper as fe
import Graded1.DecisionTree as tree


def createRandomTrees(number, data):
    trees = []

    for i in range(number):
        features = ['Sex', 'Family_size', 'Age', 'Pclass', 'CabinBool', 'Embarked', 'SibSp', 'Parch', 'Alone']
        tree1 = tree.Tree()
        tree1.createRandomTree(data, features)
        trees.append(tree1)
    return trees

def combineResults(data):
    print(len(data))
    result = []
    for i in range(len(data[0])):
        numSurvived = 0
        numDied = 0
        for j in range(len(data)):
            if data[j][i] == 1:
                numSurvived += 1
            else:
                numDied += 1
        if numSurvived > numDied:
            result.append(1)
        else:
            result.append(0)
    return result

def getResult(treeRnd):
    survived = treeRnd.evealuteData(train_data_edited)
    actualSurvived = []
    for entry in train_data_edited:
        actualSurvived.append(int(entry['Survived']))

    counter = 0
    for i in range(len(survived)):
        if survived[i] == actualSurvived[i]:
            counter += 1

    print(counter / len(actualSurvived))


processor = dp.DataProc()
feature_processor = fe.FeatureEngineer()

train_data = processor.get('train.csv')

train_data_edited = feature_processor.createAwesomeDataset(train_data)

#Features to use for decision tree
features = ['Sex', 'Family_size', 'Age', 'Pclass', 'CabinBool', 'Embarked'] #  'Title'
#Create a tree with given trainingsdata and selected features
tree1 = tree.Tree()
tree1.createTree(train_data_edited, features)




#First evaluation
survived = tree1.evealuteData(train_data_edited)

trees = createRandomTrees(100, train_data_edited)
data = []
for treeRnd in trees:
    data.append(treeRnd.evealuteData(train_data_edited))
    getResult(treeRnd)
survived = combineResults(data)

print(train_data_edited)

#Load and evaluate test data o.o
test_data = processor.get("test.csv")
test_data_edited = feature_processor.createAwesomeDataset(test_data)

survivedTest = tree1.evealuteData(test_data_edited)

data = []
for treeRnd in trees:
    data.append(treeRnd.evealuteData(test_data_edited))
    getResult(treeRnd)
survivedTestRnd = combineResults(data)

actualSurvived = []
for entry in train_data_edited:
    actualSurvived.append(int(entry['Survived']))

counter = 0
for i in range(len(survived)):
    if survived[i] == actualSurvived[i]:
        counter += 1

print(counter / len(actualSurvived))

f = open('pred.csv', 'w')
f.write('PassengerId,Survived\n')  # python will convert \n to os.linesep
for i in range(len(test_data_edited)):
    f.write(test_data_edited[i]['PassengerId'] + "," + str(survivedTestRnd[i]) + "\n")
f.close()
