class Node:


    def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


    def __str__(self):
        return self.prev.__str__, self.data.__str__, self.next.__str__