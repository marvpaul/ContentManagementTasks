import math
import Graded1.Node as Node
class Tree:
    '''Decision tree class which in represented by a root node dataTree'''
    dataTree = None

    def evealuteData(self, data):
        '''
        Requirement: A builded decisiontree
        This evaluates a set of entries (data) with the created decisiontree
        :param data: the data for each passenger of the titanic
        :return: an array with classes. 1: Survived, 0: died
        '''
        if self.dataTree == None:
            raise ValueError
        else:
            survived = []
            for entry in data:
                survived.append((self.getDecision(self.dataTree, entry)))
            return survived

    def getDecision(self, node, entry):
        '''
        This is a recursive method to go through a given decision tree and determine which class the tree classifies
        :param node: the acutal node
        :param entry: the entry which is currently evaluated
        :return: survived: 1, died: 0
        '''
        if node.feature == "Survived":
            return node.decisions[0]
        elif entry[node.feature] in node.decisions:
            return self.getDecision(node.following_nodes[node.decisions.index(entry[node.feature])], entry)

    def createTree(self, data, features):
        '''
        Method to determine the hopefully best fitting decision tree for given data & features
        :param data: given trainingsdata
        :param features: the features we want to split for as an array, f.e. ['Sex', 'Age']
        '''
        entropies = []
        for feature in features:
            entropies.append(self.getEntireEntropy(self.getPropRec(data, [feature])))
        min_value = min(entropies)
        min_index = entropies.index(min_value)
        self.dataTree = Node.Node(features[min_index])
        self.getTreeRec(data, features, self.dataTree)


    '''
    
    '''
    def getTreeRec(self, data, features, node):
        '''
        This method calculates the hopefully best decision tree for given features and data :)
        See createTree. This is just the recursive method to iterate over each node
        :param data: given trainingsdata
        :param features: the features we want to split for as an array, f.e. ['Sex', 'Age']
        :param node: the last node we have determined
        '''
        #This feature is obsolete / used
        localFeatures = features
        localFeatures.remove(node.feature)

        data, labels = self.splitData(data, node.feature)
        #For each possible decision get the best fitting feature
        for label_nr in range(len(labels)):
            entropies = []
            for feature in localFeatures:
                entropies.append(self.getEntireEntropy(self.getPropRec(data[label_nr], [feature])))
            min_value = min(entropies)
            min_index = entropies.index(min_value)

            nextNode = Node.Node(features[min_index])
            node.following_nodes.append(nextNode)
            node.decisions.append(labels[label_nr])
            if len(localFeatures) > 1:
                self.getTreeRec(data[label_nr], localFeatures, nextNode)
            #end reached
            else:
                nextNode.feature = "Survived"
                sub_data = data[label_nr]
                props_survived = self.computeSurvivalProp(sub_data)
                if props_survived[0] > props_survived[1]:
                    nextNode.decisions = [0]
                else:
                    nextNode.decisions = [1]

    def computeEntropy(self, probs):
        '''
        Calculate entropy for some props - nothing fancy here
        :param probs: Some props [0.9, 0.5, 0.4]
        :return: Returns the entropy
        '''
        propability = 0
        for p in probs:
            if p != 0:
                propability -= p * math.log2(p)
        return propability

    def getEntireEntropy(self, props):
        '''
        This method computes the entire entropy where props is an array with entries like [[prop1, prop2], occurence]
        :param props: array with [[prop1, prop2], occurence]
        :return: an entropy :)
        '''
        entireEntropy = 0
        for prop in props:
            entireEntropy += self.computeEntropy(prop[0]) * prop[1]
        return entireEntropy


    '''
    '''
    def computeSurvivalProp(self, data):
        '''
        This function compute the probabilities for case survived | not survived
        :param data: a given dataset
        :return: [propDied, propSurvived]
        '''
        props = []
        size = len(data)
        amount_class1 = 0
        amount_class2 = 0
        for entry in data:
            if int(entry['Survived']) == 0:
                amount_class1 += 1
            else:
                amount_class2 += 1
        props.append(amount_class1 / size)
        props.append(amount_class2 / size)
        return props

    def getPropRec(self, data, features):
        '''
        This function get the props for each class. The data is splitted for each feature
        F.e. features = [Age, Sex], then the data will be splitted into Age, then Sex and then calculate all props for classes
        :param data: the trainingsdata
        :param features: the feature we want to split for In exact this order: firstFeatureToSplit .... lastFeatureToSplit
        :return: some props (Y)
        '''
        #In case there is no more feature we have to split for return the prop
        if len(features) == 0:
            return self.computeSurvivalProp(data)
        else:
            #Split the data into feateures[0] values
            splittedData, labels = self.splitData(data, features[0])
            props = []
            if len(features)-1 == 0:
                for i in range(len(splittedData)):
                    props.append([self.getPropRec(splittedData[i], features[1:len(features)]), len(splittedData[i]) / len(data)])
            else:
                for i in range(len(splittedData)):
                    props.append(self.getPropRec(splittedData[i], features[1:len(features)]))
            return props

    def splitData(self, data, feature):
        '''
        Split data into n groups of different feature values
        Example: data = ['male', 'female'], splittedData = [['male'], ['female']]
        :param data: ['maleData', 'femaleData']
        :param feature: the feature for which one we want to split
        :return: splittedData = [['maleData'], ['femaleData']]
        '''
        differentValues = []
        for entry in data:
            if entry[feature] not in differentValues:
                differentValues.append(entry[feature])
        splittedData = []
        for i in range(len(differentValues)):
            splittedData.append([])
        for entry in data:
            splittedData[differentValues.index(entry[feature])].append(entry)
        return splittedData, differentValues

'''
Hopefully not necessary anymore :)
    This just normalize the prop data, because there where some problem while storing them in a list in the recursion
    prop_norm = []
    def norm_props(self, props):
        for prop in props:
            if len(prop) == 2 and type(prop[0]) is list and type(prop[1]) is float:
                self.prop_norm.append(prop)
            else:
                self.norm_props(prop)
        return self.prop_norm
'''