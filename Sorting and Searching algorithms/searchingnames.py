from binarysearch import *
import random

def returnnameslist(length):
    list1 = [None] * length
    #names generated using OpenAI generative AI
    names = ["Alice", "Olivia", "Emma", "Sophia", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail", "Ella", "Scarlett", "Grace", "Lily", "Aria", "Chloe", "Madison", "Emily", "Charlotte", "Zoe", "Hannah", "Ellie", "Layla", "Avery", "Sofia", "Camila", "Victoria", "Riley", "Nora", "Mila", "Aubrey", "Scarlett", "Stella", "Natalie", "Leah", "Hazel", "Lucy", "Penelope", "Lillian", "Addison", "Eleanor", "Bella", "Audrey", "Brooklyn", "Alice", "Savannah", "Caroline", "Kennedy", "Genesis", "Skylar", "Violet", "Claire", "Lucy", "Anna", "Leah", "Naomi", "Sarah", "Allison", "Gabriella", "Alice", "Audrey", "Peyton", "Sophie", "Hailey", "Sadie", "Eva", "Ruby", "Elena", "Caroline", "Allison", "Maya", "Autumn", "Mackenzie", "Kennedy", "Alexis", "Julia", "Paisley", "Arianna", "Sadie", "Bella", "Gianna", "Aurora", "Hannah", "Isla", "Maria", "Everly", "Claire", "Ruby", "Ivy", "Eliza", "Lucy", "Quinn", "Allison", "Nora", "Violet", "Clara", "Emilia", "Eliana", "Zoey", "Lucy", "Addison", "Emery", "Madeline", "Kayla", "Paige", "Hailey", "Avery", "Stella", "Rylee", "Finley", "Naomi", "Jordyn", "Lydia", "Willow", "Emma", "Sadie", "Faith", "Rachel", "Natalie", "Bella", "Marley", "Addison", "Maya", "Skylar", "Victoria", "Camila", "Sophie", "Ariana"]
    for i in range(length):
        temp = random.choice(names)
        list1[i] = temp
        names.remove(temp)
    return list1


def convertnames(list1):
    for i in range(len(list1)):
        temp = 0
        for char in list1[i]:
            temp = temp + ord(char)
        list1[i] = temp
    return list1


list1 = returnnameslist(100)
search_name = random.choice(list1)
print("Finding", search_name,"in",list1,"\n" )

list2 = convertnames(list1)
list2.sort()
search_name2 = random.choice(list2)

search_name = random.choice(list1)
print("Finding", search_name)

temp = binarysearch(list1, search_name)
print("Found")
