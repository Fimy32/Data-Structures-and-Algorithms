from hashtable.hashtable import HashTable
from queue import Queue
import json

current = 0
enquiries = Queue()
POI_Hashtable = HashTable()
POI_Hashtable.add("Railway Station",("Transport","A train station with 4 platforms."))
POI_Hashtable.add("Park Cafe",("Restaurant","A Cafe with free coffee refills."))
POI_Hashtable.add("War Memorial",("Memorial","Statue dedicated to those who were lost."))
POI_Hashtable.add("White Horse Pub",("Restaurant","A pub that serves food before 9:30PM."))
#with open("assessment/pois.json","r") as file:




def menu():
    global current
    with open("assessment/pois.json","w") as file:
        json.dump(POI_Hashtable.getall(),file)
    options = [("Add a POI",add),("Search a POI",search),("Remove a POI",delete),("Show all POIs",showall),("Add an Enquiry",enquiry),("Answer an Enquiry",answer),("Exit",)]
    print("\n")
    for i in range(len(options)):
        if i == current:
            print("[~" + options[i][0].upper(), end="~] ")
        else:
            print("|",options[i][0], end=" | ")
    option = input("\n\nWould you like to " + options[current][0] + "?\n\n<         Y        >\n\n")
    if option == "Y" and options[current][0] == "Exit":
        return False
    elif option == "Y":
        options[current][1]()
        return True
    elif option == "<":
        if current == 0:
            current = 6
        else:
            current -= 1
        return True
    else:
        if current == 6:
            current = 0
        else:
            current += 1
        return True

def add():
    print(POI_Hashtable.add(input("Please Enter POI Name "),(input("Please Enter POI type "),input("Please Enter POI Desc "))))

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
    #currentq = enquiries.peek()
    print(enquiries.peek())
    enquiries.pop()
    print("Remaining Queries: " + str(enquiries.return_remaining()))
