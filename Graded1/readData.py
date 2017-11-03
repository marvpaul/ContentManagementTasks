import Graded1.dataProcessingHelper as dp
import Graded1.FeatureEngeneeringHelper as fe
import Graded1.DecisionTree as tree

processor = dp.DataProc()
feature_processor = fe.FeatureEngineer()

train_data = processor.get('train.csv')

train_data_edited = feature_processor.createAwesomeDataset(train_data)

#Features to use for decision tree
features = ['Sex', 'Age', 'Family_size', 'Embarked', 'Cabin', 'AgeClass', 'FareClass'] #Title, Pclass

#Create a tree with given trainingsdata and selected features
tree1 = tree.Tree()
tree1.createTree(train_data_edited, features)

#First evaluation
survived = tree1.evealuteData(train_data_edited)



#Load and evaluate test data o.o
test_data = processor.get("test.csv")
test_data_edited = feature_processor.createAwesomeDataset(test_data)

survivedTest = tree1.evealuteData(test_data_edited)

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
    f.write(test_data_edited[i]['PassengerId'] + "," + str(survivedTest[i]) + "\n")
f.close()
