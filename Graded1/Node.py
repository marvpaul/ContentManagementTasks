class Node:
    '''
    This is a class which represents a node in a tree
    '''

    def __init__(self, feature):
        self.feature = feature
        self.following_nodes = []
        self.decisions = []

    def setFollowingNode(self, follow):
        self.following_nodes.append(follow)