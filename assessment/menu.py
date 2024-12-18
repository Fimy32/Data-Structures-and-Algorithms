from hashtable.hashtable import HashTable
from queue import Queue
import json
from binarytree import BinaryTree
import pois_text_file; pois_text = pois_text_file.pois

current = 0
enquiries = Queue()
POI_Hashtable = HashTable()

route = BinaryTree()
route.insert((ord("g"),"Railway Station"))
route.insert((ord("u"),"West Quay"))
route.insert((ord("a"),"Park Cafe"))
route.insert((ord("l"),"Mcdonalds"))
route.insert((ord("P"),"White Horse Pub"))
route.insert((ord("i"),"War Memorial"))
route.insert((ord("m"),"Southampton Common"))

for element in pois_text:
    POI_Hashtable.add(element[0],(element[1],element[2]))

def menu():
    global current
    templist = []
    for element in POI_Hashtable.getall():
        templist.append(str(element))

    with open("assessment/pois_text_file.py","w") as file:
        file.write("pois = [")
        for element in templist:
            file.write(f"{element},")
        file.write("]")


    options = [("Add a POI",add),("Search a POI",search),("Remove a POI",delete),("Show all POIs",showall),("Find a Route",routing),("Add an Enquiry",enquiry),("Answer an Enquiry",answer),("Exit",)]
    print("\n")
    for i in range(len(options)):
        if i == current:
            print("[>" + options[i][0].upper(), end="<\n")
        else:
            print("|",options[i][0], end="  \n")
    option = input("\n\nWould you like to " + options[current][0] + "?\n\n<         Y        >\n\n")
    print("\n" * 20)
    if option == "Y" and options[current][0] == "Exit":
        return False
    elif option == "Y":
        options[current][1]()
        return True
    elif option == "<":
        if current == 0:
            current = 7
        else:
            current -= 1
        return True
    else:
        if current == 7:
            current = 0
        else:
            current += 1
        return True

def add():
    print(POI_Hashtable.add(input("Please Enter POI Name "), (input("Please Enter POI type "), input("Please Enter POI Desc "))))

def search():
    print("Found", POI_Hashtable.get(input("Please Enter POI Name ")))

def delete():
    print(POI_Hashtable.delete(input("Name to Remove: ")))

def showall():
    print("Showing all POIs sorted by their Name:")
    for POI in POI_Hashtable.getall():
        print("\n" + POI)

def enquiry():
    enquiries.push(input("Enter your enquiry: "))

def answer():
    if enquiries.return_remaining() >0:
        print(enquiries.peek())
        enquiries.pop()
        print("Remaining Queries: " + str(enquiries.return_remaining()))
    else:
        print("No More Queries Remain")

def routing():
    routefind = input("Enter name of POI to route to from the train station. This only works with the initial POIs: ")
    route.search((ord(routefind[len(routefind) - 3]),routefind))




