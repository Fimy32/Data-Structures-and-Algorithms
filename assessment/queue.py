from hashtable.linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.internalList = LinkedList()
        self.id = 0
        self.remaining = 0

    def push(self, item):

        self.internalList.add(str(self.id),("Query",item))
        self.id += 1
        self.remaining += 1

    def pop(self,):
        counter = 0
        while self.internalList.get(counter) is None:
            counter = counter + 1
        self.internalList.deletenode(counter)
        self.remaining -= 1



    def peek(self):
            counter = 0
            while self.internalList.get(counter) is None:
                counter = counter + 1
            return self.internalList.get(counter)

    def return_remaining(self):
         return self.remaining
    
    def __str__(self):

        return self.internalList.__str__()