class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = (key, value)

    def link(self, otherNode):
        self.next = otherNode
        otherNode.prev = self
    def delete(self):
        self.value = (None,(None,None))
    def __str__(self):
        return str((self.value[0], self.value[1][0], self.value[1][1]))