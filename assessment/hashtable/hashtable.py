from linkedlist import LinkedList

class HashTable:
    def __init__(self,):
        self.buckets = [LinkedList() for i in range(127)]

    def hash(self, key):
        totalhash = ""
        for i in range(len(key)):
            for char in key:
                totalhash += (ord(char) * 31) ^ i
            return totalhash

    def add(self, key, value):
        self.buckets[hash(key) % 127].add(key, value)
        return "Added",key,value

    def delete(self, key):
        for i in range(self.buckets[hash(key) % 127].size):
            total = ""
            for g in range(len(key)):
                total += self.buckets[hash(key) % 127].get(i)[g]
        return "Deleted", total
    
    def get(self, key):
        for i in range(self.buckets[hash(key) % 127].size):
            total = ""
            for g in range(len(key)):
                total += self.buckets[hash(key) % 127].get(i)[g]
        return total
