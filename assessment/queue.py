from hashtable.linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.internalList = LinkedList()
        self.id = 0
        self.remaining = 0
        self.counter = 0

    def push(self, item):

        self.internalList.add((item),("ID:",str(self.id)))
        self.id += 1
        self.remaining += 1

    def pop(self,):
        
        while self.internalList.getnonspecific(self.counter) is None:
            self.counter = self.counter + 1
        self.internalList.deletefirstnode(self.counter)
        self.remaining -= 1



    def peek(self):
            
            while self.internalList.getnonspecific(self.counter) is None:
                self.counter = self.counter + 1
            return self.internalList.getnonspecific(self.counter)

    def return_remaining(self):
         return self.remaining
    
    def __str__(self):

        return self.internalList.__str__()