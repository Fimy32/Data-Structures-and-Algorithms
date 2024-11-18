from node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, key, value):
        n = Node(key, value)
        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.link(n)
            self.last = n
        self.size += 1

    def get(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                return currentNode
            else:
                currentNode = currentNode.next
                counter += 1
        return currentNode.value[1]
    

    def find(self, key):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[0] == key:
                return currentNode.value[1]
            else:
                currentNode = currentNode.next
        return None