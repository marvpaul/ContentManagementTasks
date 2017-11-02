import math
import Graded1.Node as Node
class Tree:
    dataTree = None

    #TODO: This have to be a recursive method call for creating a nice tree :)
    def getFirstFeatureToSplit(self, data, features):
        entropies = []
        for feature in features:
            entropies.append(self.getEntireEntropy(self.getPropRec(data, [feature])))
        min_value = min(entropies)
        min_index = entropies.index(min_value)
        print("Oh yeah! The best decision is to split for" + features[min_index])
        self.dataTree = Node.Node(features[min_index])
        self.getSecondFeatureToSplit(data, features, self.dataTree)


    def getSecondFeatureToSplit(self, data, features, node):
        #This feature is obsolete / used
        features.remove(self.dataTree.feature)

        data, labels = self.splitData(data, self.dataTree.feature)
        #For each possible decision get the best fitting feature
        for label_nr in range(len(labels)):
            entropies = []
            for feature in features:
                entropies.append(self.getEntireEntropy(self.getPropRec(data[label_nr], [feature])))
            min_value = min(entropies)
            min_index = entropies.index(min_value)
            node.following_nodes.append(Node.Node(feature[min_index]))
            node.decisions.append(labels[label_nr])
            print("Oh yeah! The best decision is to split for" + features[min_index])
            print(min_value, labels[label_nr])





    '''
    Given: Some props [0.9, 0.5, 0.4]
    Returns the entropy
    '''
    def computeEntropy(self, probs):
        propability = 0
        for p in probs:
            if p != 0:
                propability -= p * math.log2(p)
        return propability


    '''
    This method computes the entire entropy where props is an array with entries like [[prop1, prop2], occurence]'''
    def getEntireEntropy(self, props):
        entireEntropy = 0
        for prop in props:
            entireEntropy += self.computeEntropy(prop[0]) * prop[1]
        return entireEntropy


    '''
    This function compute the probabilities for case survived | not survived'''
    def computeProps(self, data):
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

    '''
    This function get the props for each class. The data is splitted for each feature
    F.e. features = [Age, Sex], then the data will be splitted into Age, then Sex and then calculate all props for classes'''
    def getPropRec(self, data, features):
        #In case there is no more feature we have to split for
        if len(features) == 0:
            return self.computeProps(data)
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

    '''
    Split data into n groups of different feature values
    Example: data = ['male', 'female'], splittedData = [['male'], ['female']]'''
    def splitData(self, data, feature):
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
    This just normalize the prop data, because there where some problem while storing them in a list in the recursion
    '''
    prop_norm = []
    def norm_props(self, props):
        for prop in props:
            if len(prop) == 2 and type(prop[0]) is list and type(prop[1]) is float:
                self.prop_norm.append(prop)
            else:
                self.norm_props(prop)
        return self.prop_norm
