class Node:
    '''
    This is a class which represents a node in a tree
    '''

    def __init__(self, feature):
        '''
        Constructor
        :param feature: the feature / name of the node
        '''
        self.feature = feature
        self.following_nodes = []
        self.decisions = []