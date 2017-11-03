import csv

class DataProc:
    '''
    This is a class which help processing the given data
    '''
    def readData(self, path):
        '''
        Read the data + header of a given csv file
        :param path: the path for csv
        :return: tuple, header, data
        '''
        data = []
        header = ""
        with open(path, 'r') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            header = next(reader)
            data = []
            for row in reader:
                data.append(row)
        return header, data

    def createDic(self, header, data):
        '''
        Create a dict where each entry in header is a key
        :param header: represent keys in the dict
        :param data: the data :)
        :return: a beautiful dictionary
        '''
        dic = {}
        new_data = []
        for entry in data:
            for value_number in range(len(entry)):
                dic[header[value_number]] = entry[value_number]
            new_data.append(dic)
            dic = {}
        return new_data

    def get(self, path):
        '''
        Just convert a csv file into a python dic
        :param path: path for csv file
        :return:
        '''
        header, data = self.readData(path)
        return self.createDic(header, data)