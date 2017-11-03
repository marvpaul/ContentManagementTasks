import re
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
            elif float(entry['Age']) <= 5:
                entry['Age'] = "1"
            elif float(entry['Age']) <= 12:
                entry['Age'] = "2"
            elif float(entry['Age']) <=18:
                entry['Age'] = "3"
            elif float(entry['Age']) <= 24:
                entry['Age'] = "4"
            elif float(entry['Age']) <= 50:
                entry['Age'] = "5"
            else:
                entry['Age'] = "6"
        return data

    def categorizeCabin(self, data):
        '''
        Categorize cabine
        :param data:
        :return:
        '''
        for entry in data:
            '''
            if "A" in entry['Cabin'] or "B" in entry['Cabin'] or "C" in entry['Cabin']:
                entry['Cabin'] = 1
            elif "D" in entry['Cabin'] or "E" in entry['Cabin']:
                entry['Cabin'] = 2
            else:
                entry['Cabin'] = 3
            '''
            if entry['Cabin'] == "":
                entry['Cabin'] = 0
            else:
                entry['Cabin'] = 1
        return data

    def fillEmbarkedFeature(self, data):
        for entry in data:
            '''
            if "A" in entry['Cabin'] or "B" in entry['Cabin'] or "C" in entry['Cabin']:
                entry['Cabin'] = 1
            elif "D" in entry['Cabin'] or "E" in entry['Cabin']:
                entry['Cabin'] = 2
            else:
                entry['Cabin'] = 3
            '''
            if entry['Embarked'] == "S":
                entry['Embarked'] = 1
            elif entry['Embarked'] == "C":
                entry['Embarked'] = 2
            elif entry['Embarked'] == "Q":
                entry['Embarked'] = 3
            else:
                #Entry is empty, so fill with the most common value S / 1
                entry["Embarked"] = 1
        return data

    def filterTitles(self, data):
        '''
        Filter titles from name and categorized as mentioned here: https://www.kaggle.com/nadintamer/titanic-survival-predictions-beginner
        :param data:
        :return:
        '''
        for entry in data:
            title = re.search(' ([A-Za-z]+)\.', entry['Name']).group(1)
            title.replace('Lady', 'Rare')
            title.replace('Capt', 'Rare')
            title.replace('Col', 'Rare')
            title.replace('Don', 'Rare')
            title.replace('Dr', 'Rare')
            title.replace('Major', 'Rare')
            title.replace('Rev', 'Rare')
            title.replace('Jonkheer', 'Rare')
            title.replace('Dona', 'Rare')
            title.replace('Countess', 'Royal')
            title.replace('Lady', 'Royal')
            title.replace('Sir', 'Royal')
            title.replace('Mlle', 'Miss')
            title.replace('Ms', 'Miss')
            title.replace('Mme', 'Mrs')
            entry['Title'] = title
        return data

    def categorizeFare(self, data):
        '''
        :param data:
        :return:
        '''
        sum = 0
        missing = 0
        for entry in data:
            if(entry['Fare'] == ""):
                missing += 1
            else:
                sum += float(entry['Fare'])
        mean = sum / (len(data)-missing)
        mean_low = mean - (mean * 0.66)
        mean_high = mean + (mean *0.66)
        for entry in data:
            if(entry['Fare'] == ""):
                entry['FareClass'] = 1
            elif float(entry['Fare']) < mean_low:
                entry['FareClass'] = 0
            elif float(entry['Fare']) >= mean_low and float(entry['Fare']) <= mean_high:
                entry['FareClass'] = 1
            else:
                entry['FareClass'] = 2
        return data

    def createAwesomeDataset(self, data):
        '''
        Do some awesome stuff to make the given data "better"
        :param data: given dataset
        :return: a better dataset :)
        '''
        data = self.addFamilySizeFeature(data)
        simplifiedData = self.deleteUnimportantData(data, ["Ticket"])
        simplifiedData = self.categorizeAge(simplifiedData)
        simplifiedData = self.categorizeCabin(simplifiedData)
        simplifiedData = self.fillEmbarkedFeature(simplifiedData)
        simplifiedData = self.filterTitles(simplifiedData)
        simplifiedData = self.categorizeFare(data)
        return simplifiedData
