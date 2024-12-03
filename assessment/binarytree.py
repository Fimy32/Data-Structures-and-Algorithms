from binarynode import Node

class BinaryTree:
    def __init__(self):
        self.first = None
        self.test = []

    def insert(self, value):
        if self.first is None:
            self.first = Node(value)
        else:
            self.first.recursiveinsert(value)
            self.test.append(value)

    def printify(self):
        self.first.recursiveprint(0)

    def search(self, value):
        self.first.search(value,1)