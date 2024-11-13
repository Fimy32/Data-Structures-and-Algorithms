import random


def getlist(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(1,50))
    return list1

def getrandomsearch(list1):
    return random.choice(list1)

def binarysearch(list1,searchparameter):
    middle = list1[len(list1)//2]
    while middle != searchparameter:
        if middle < searchparameter:
            for i in range(len(list1)//2,len(list1)):
                list1.remove(list1[0])
        else:
            for i in range(0,len(list1)//2):
                list1.pop()
        middle = list1[len(list1) // 2]
        print("Finding",searchparameter,"Current",middle,list1)
    return middle





# list1 = getlist(50)
# list1.sort()
# print("Found,",binarysearch(list1,getrandomsearch(list1)))