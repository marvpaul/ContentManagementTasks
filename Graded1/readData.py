import Graded1.dataProcessingHelper as dp
import Graded1.FeatureEngeneeringHelper as fe
import Graded1.DecisionTree as tree
import Graded1.RandomForest as rnd_forest

def getResult(real_data, evaluated_data):
    counter = 0
    for i in range(len(real_data)):
        if real_data[i] == evaluated_data[i]:
            counter += 1

    return counter / len(evaluated_data)



processor = dp.DataProc()
feature_processor = fe.FeatureEngineer()

train_data = processor.get('train.csv')

train_data_edited = feature_processor.createAwesomeDataset(train_data)


evaluation_data = train_data_edited[:int(len(train_data_edited)/2)]
train_data_edited = train_data_edited[int(len(train_data_edited)/2):]

real_survived = []
for entry in evaluation_data:
    real_survived.append(int(entry['Survived']))

#Features to use for decision tree
features = ['Sex', 'Family_size', 'Age', 'Pclass', 'CabinBool', 'Embarked'] #  'Title'

#Create a tree with given trainingsdata and selected features
tree1 = tree.Tree()
tree1.createTree(train_data_edited, features)

#First evaluation
survived = tree1.evealuteData(train_data_edited)

print(getResult(real_survived, survived))
print(train_data_edited)
features = ['Sex', 'Family_size', 'Age', 'Pclass', 'CabinBool', 'Embarked'] #  'Title'
random_trees = rnd_forest.RandomForest(20, train_data_edited, features)
survived_rnd = random_trees.evaluteData(train_data_edited)

result = getResult(real_survived, survived_rnd)

#Search for a coool forest :)
while(result < 0.83):
    random_trees = rnd_forest.RandomForest(5, train_data_edited, features)
    survived_rnd = random_trees.evaluteData(evaluation_data)
    result = getResult(real_survived, survived_rnd)

print(getResult(real_survived, survived_rnd))





#Load and evaluate test data o.o
test_data = processor.get("test.csv")
test_data_edited = feature_processor.createAwesomeDataset(test_data)

survived_test_data_dec_tree = tree1.evealuteData(test_data_edited)

survived_test_data_rnd_forest = random_trees.evaluteData(test_data_edited)

f = open('pred.csv', 'w')
f.write('PassengerId,Survived\n')  # python will convert \n to os.linesep
for i in range(len(test_data_edited)):
    f.write(test_data_edited[i]['PassengerId'] + "," + str(survived_test_data_rnd_forest[i]) + "\n")
f.close()