class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = (key, value)

    def link(self, otherNode):
        self.next = otherNode
        otherNode.prev = self

    def __str__(self):
        return str(("Name:", self.value[0], "Type:",self.value[1][0], "Desc:",self.value[1][1]))