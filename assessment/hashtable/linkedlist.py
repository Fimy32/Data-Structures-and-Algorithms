from hashtable.node import Node

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
                if currentNode.value[0] == None:
                    return None
                elif currentNode.prev != None:
                    while input("Is this the POI you were looking for? " + str(currentNode) + " Y/N\n") != "Y":
                        if currentNode.prev is None:
                            print("\nNo other POI with that name found!\n")
                        else:
                            currentNode = currentNode.prev
                    return str(currentNode)
                else:
                    return str(currentNode)
            else:
                currentNode = currentNode.next
                counter += 1
        return None
    
    def getnonspecific(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                if currentNode.value[0] == None:
                    return None
                else:
                    return str(currentNode)
            else:
                currentNode = currentNode.next
                counter += 1
        return None
    
    
    def deletenode(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                if currentNode.value[0] == None:
                    return None
                elif currentNode.prev != None:
                    while input("Is this the POI you were looking for? " + str(currentNode) + " Y/N") != "Y":
                        if currentNode.prev is None:
                            print("\nNo other POI with that name found!\n")
                        else:
                            currentNode = currentNode.prev
                    return str(currentNode)
                else:
                    return str(currentNode)
            else:
                currentNode = currentNode.next
                counter += 1
        return None
    
    def deletefirstnode(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                if currentNode.value[0] == None:
                    return None
                else:
                    return currentNode.delete()
            else:
                currentNode = currentNode.next
                counter += 1
        return None

    def find(self, key):
        currentNode = self.first
        while currentNode is not None:    
            if currentNode.next != None:
                while input("Is this the POI you were looking for? " + str(currentNode) + " Y/N") != "Y":
                    if currentNode.next is None:
                        print("\nNo other POI with that name found!\n")
                    else:
                        currentNode = currentNode.next
                return currentNode
            elif currentNode.value[0] == key:
                return currentNode
            else:
                currentNode = currentNode.next
        return None
    
    def delete(self,key):
        if key is int:
            self.get(key).value = (None,("None,None"))
        else:
            self.find(key).value = (None,("None,None"))


        
    