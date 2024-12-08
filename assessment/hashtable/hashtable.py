from hashtable.linkedlist import LinkedList
from insertionsort import *

class HashTable:
    def __init__(self,):
        self.buckets = [LinkedList() for i in range(127)]

    def hash(self, key):
        totalhash = 0
        for i in range(len(key)):
            for char in key:
                totalhash += (ord(char) * 31) ^ i
            return totalhash

    def add(self, key, value):
        self.buckets[hash(key) % 127].add(key, value)
        return "Added",key,value

    def delete(self,key):
        self.buckets[hash(key) % 127].delete(key)
        return "Deleted",key

    def get(self, key):
        for i in range(self.buckets[hash(key) % 127].size):
            total = ""
            for g in range(len(key)):
                total += self.buckets[hash(key) % 127].get(i)
        return total

    def getall(self,):
        all = []
        for bucket in self.buckets:
            if bucket is not None:
                for i in range(bucket.size):
                    if bucket.get(i) is not None:
                        all.append((ord(bucket.get(i)[2]),bucket.get(i)))
        all = insertionsort(all)
        if len(all) == 0:
            return "No POIs Found"
        else:
            temp = []
            for element in all:
                temp.append(element[1])
            return temp