import Graded1.dataProcessingHelper as dp
import Graded1.FeatureEngeneeringHelper as fe
import Graded1.DecisionTree as tree

def getResult(real_data, evaluated_data):
    counter = 0
    for i in range(len(real_data)):
        if real_data[i] == evaluated_data[i]:
            counter += 1

    return counter / len(evaluated_data)

def loadAndEvaluateTestData(tree1):
    '''
    Load and evaluate the test data and save them into pred.csv ready for submitting to kaggle
    :param tree1: a decision tree or a random forest
    :return: nothing but makes the job :)
    '''
    test_data = processor.get("test.csv")
    test_data_edited = feature_processor.createAwesomeDataset(test_data)

    survived_pred = tree1.evealuteData(test_data_edited)

    f = open('pred_dec_tree.csv', 'w')
    f.write('PassengerId,Survived\n')  # python will convert \n to os.linesep
    for i in range(len(test_data_edited)):
        f.write(test_data_edited[i]['PassengerId'] + "," + str(survived_pred[i]) + "\n")
    f.close()

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
pred_survived = tree1.evealuteData(train_data_edited)


real_survived = []
for entry in train_data_edited:
    real_survived.append(int(entry['Survived']))


print(getResult(real_survived, pred_survived))

loadAndEvaluateTestData(tree1)



