class Stack:
    def __init__(self):
        self.internalList = []

    def push(self, item):

        self.internalList.append(item)


    def pop(self):

        if len(self.internalList) > 0:
            temp = self.internalList[-1]
            self.internalList.pop()
        else:
            raise Exception("not enough items in stack to pop. items must be more than or equal to 1")
        return temp


    def peek(self):

        return self.internalList[-1]


    def __str__(self):

        return self.internalList.__str__()