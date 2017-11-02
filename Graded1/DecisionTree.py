import math
import Graded1.Node as Node
class Tree:
    dataTree = None

    def evealuteData(self, data):
        survived = []
        for entry in data:
            actualNode = self.dataTree

            survived.append((self.getDecision(actualNode, entry)))
        return survived

    def getDecision(self, node, entry):
            if node.feature == "Survived":
                return node.decisions[0]
            elif entry[node.feature] in node.decisions:
                return self.getDecision(node.following_nodes[node.decisions.index(entry[node.feature])], entry)
            #TODO: Get a better idea what todo here
            print("Sth")
            return 0

    '''
    Recursive method to determine the hopefully best fitting decision tree for given data & features'''
    def getTree(self, data, features):
        entropies = []
        for feature in features:
            entropies.append(self.getEntireEntropy(self.getPropRec(data, [feature])))
        min_value = min(entropies)
        min_index = entropies.index(min_value)
        self.dataTree = Node.Node(features[min_index])
        self.getTreeRec(data, features, self.dataTree)


    '''
    This method calculates the hopefully best decision tree for given features and data :)
    '''
    def getTreeRec(self, data, features, node):
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
                nextNode.decisions = [self.survivedOrNot(data[label_nr])]


    '''Return 1 if most of the data entry people have survived'''
    def survivedOrNot(self, data):
        amount_class1 = 0
        amount_class2 = 0
        for entry in data:
            if int(entry['Survived']) == 0:
                amount_class1 += 1
            else:
                amount_class2 += 1
        if amount_class2 > amount_class1:
            return 1
        return 0


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
