import Graded1.DecisionTree as tree

class RandomForest:
    random_forest = None
    accuracies = []

    #The results we know about - TODO: Split trainingsdata into train and test data to get a better accuracy
    test_results = []

    def __init__(self, number_trees, data, features) -> None:
        '''
        Creates number_trees random trees and add them to the instance var random_forest
        :param number_trees: the number of trees to create
        :param data: the titanic dataset
        :param features: some awesome features which will be used to create a tree
        '''
        super().__init__()
        trees = []
        for i in range(number_trees):
            #TODO: STH went wrong here, fix this :)
            features = ['Sex', 'Family_size', 'Age', 'Pclass', 'Title', 'SibSp', 'AgeClass']#CabinBool, Embarked
            tree1 = tree.Tree()
            tree1.createRandomTree(data, features)
            trees.append(tree1)
        print("Tree created")
        self.random_forest = trees

    def evaluteData(self, test_data):

        #Evaluate data for each tree
        data = []
        for treeRnd in self.random_forest:
            tree_data = treeRnd.evealuteData(test_data)
            data.append(tree_data)
            #self.accuracies.append(self.getAccuracy(tree_data))
        result = []
        #Go through all results and decide which entry we should use with simple voting TODO: Implement voting with accuracy
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

    def getAccuracy(self, data):
        '''
        Determine how accurate the tree was with given results in test_results
        :param data: the evaluated data
        :return: accuracy as float
        '''
        actualSurvived = []
        for entry in data:
            actualSurvived.append(int(entry['Survived']))

        counter = 0
        for i in range(len(self.test_results)):
            if self.test_results[i] == actualSurvived[i]:
                counter += 1

        print(counter / len(actualSurvived))
