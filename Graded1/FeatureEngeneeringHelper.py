class FeatureEngineer:
    '''
    This class is for feature engineering
    '''
    def deleteUnimportantData(self, data, unimportantData):
        '''
        Delete data / features we don't need
        :param data: the dataset
        :param unimportantData: array with unimportant features, f.e. ['Age']
        :return:
        '''
        for entry in data:
            for key in unimportantData:
                del entry[key]
        return data

    def addFamilySizeFeature(self, data):
        '''
        Get familySize and add as new key in each entry
        FamilySize = SibSp + Parch
        :param data: given dataset
        :return: dataset with added familySize
        '''
        for entry in data:
            entry['Family_size'] = int(entry['SibSp']) + int(entry['Parch'])
        return data

    def categorizeAge(self, data):
        '''
        Because the age is a feature which is not that cool in a decision tree, just categorize the age into some
        age classes
        :param data: the give dataset
        :return: dataset with categorized age
        '''
        for entry in data:
            if entry['Age'] == "":
                entry['Age'] = "0"
            elif float(entry['Age']) <= 16:
                entry['Age'] = "1"
            elif float(entry['Age']) <= 35:
                entry['Age'] = "2"
            elif float(entry['Age']) <= 50:
                entry['Age'] = "3"
            else:
                entry['Age'] = "4"
        return data

    def categorizeCabin(self, data):
        '''
        Categorize cabine
        :param data:
        :return:
        '''
        for entry in data:
            if "A" in entry['Cabin'] or "B" in entry['Cabin'] or "C" in entry['Cabin']:
                entry['Cabin'] = 1
            elif "D" in entry['Cabin'] or "E" in entry['Cabin']:
                entry['Cabin'] = 2
            else:
                entry['Cabin'] = 3
        return data

    def createAwesomeDataset(self, data):
        '''
        Do some awesome stuff to make the given data "better"
        :param data: given dataset
        :return: a better dataset :)
        '''
        data = self.addFamilySizeFeature(data)
        simplifiedData = self.deleteUnimportantData(data, ["Name", "Ticket", "Fare", "Parch", "SibSp"])
        simplifiedData = self.categorizeAge(simplifiedData)
        simplifiedData = self.categorizeCabin(simplifiedData)
        return simplifiedData
