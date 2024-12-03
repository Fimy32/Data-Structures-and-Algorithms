class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def recursiveinsert(self,value):
        if self.data[0] > value[0]:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.recursiveinsert(value)
        elif value[0] > self.data[0]:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.recursiveinsert(value)
        else:
            pass


    def recursiveprint(self, number):
            if self.left is not None:
                self.left.recursiveprint(number + 1)
            print(str(number) + ":", self.data)
            if self.right is not None:
                self.right.recursiveprint(number + 1)

    def search(self, value, number):
        print("\n\n\nSearching: ",value, "Against:",self.data)
        print(self.left.data,self.right.data)
        if self.data == value:
            print("Found in", number, "searches!")
        elif self.data[0] < value[0]:
            self.left.search(value, number + 1)
        else:
            self.right.search(value, number + 1)
