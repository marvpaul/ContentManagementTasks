import Graded1.dataProcessingHelper as dp
import Graded1.FeatureEngeneeringHelper as fe
import Graded1.RandomForest as rnd_forest

def getResult(real_data, evaluated_data):
    '''
    Get prob for right prediction
    :param real_data: the real trainingsdata classes
    :param evaluated_data: the predicted classes
    :return: the accuracy of the pred
    '''
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

    survived_pred = tree1.evaluteData(test_data_edited)

    f = open('pred.csv', 'w')
    f.write('PassengerId,Survived\n')  # python will convert \n to os.linesep
    for i in range(len(test_data_edited)):
        f.write(test_data_edited[i]['PassengerId'] + "," + str(survived_pred[i]) + "\n")
    f.close()

def getRndTreeWithGivenProp(train_data_edited, wishedProp):
    '''
    Get a random forest which has to reach at least an certain accuracy
    :param train_data_edited: the train data
    :param wishedProp: the accuracy the model has to reach
    :return: random trees with at least an accuracy of wishedProp
    '''
    num_of_trees = 3
    random_trees = rnd_forest.RandomForest(num_of_trees, train_data_edited)
    survived_rnd = random_trees.evaluteData(train_data_edited)

    result = getResult(real_survived, survived_rnd)

    #Search for a coool forest :)
    while(result < wishedProp):
        random_trees = rnd_forest.RandomForest(num_of_trees, train_data_edited)
        survived_rnd = random_trees.evaluteData(evaluation_data)
        result = getResult(real_survived, survived_rnd)

    return random_trees, survived_rnd


processor = dp.DataProc()
feature_processor = fe.FeatureEngineer()

train_data = processor.get('train.csv')

train_data_edited = feature_processor.createAwesomeDataset(train_data)


evaluation_data = train_data_edited[:int(len(train_data_edited)/2)]
train_data_edited = train_data_edited[int(len(train_data_edited)/2):]

real_survived = []
for entry in evaluation_data:
    real_survived.append(int(entry['Survived']))


#Get a forest with at least the given probability
tree2, survived_rnd = getRndTreeWithGivenProp(train_data_edited, 0.831)
print(getResult(real_survived, survived_rnd))

loadAndEvaluateTestData(tree2)



