

class Linked_list:

    def __init__(self):
        self.first = None
        self.last = None


    def add_Node(self, node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node


    def get_Node_by_index(self, index):
        current = self.first
        for i in range(-1,index - 1):

            current = current.next
        if current is not None:
            return current
        else:
            return Exception("End Of List")

    def insert_Node_by_index(self, index, node):
        current = self.get_Node_by_index(index)
        temp = current
        node.next = temp
        node.prev = temp.prev
        current.prev.next = node
        current.next.prev = current


