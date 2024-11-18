from hashtable.hashtable import HashTable

current = 0
POI_Hashtable = HashTable()
POI_Hashtable.add("Railway Station",("Transport","A train station with 4 platforms."))
POI_Hashtable.add("Park Cafe",("Restaurant","A Cafe with free coffee refills."))
POI_Hashtable.add("War Memorial",("Memorial","Statue dedicated to those who were lost."))
POI_Hashtable.add("White Horse Pub",("Restaurant","A pub that serves food before 9:30PM."))

def menu():
    global current
    options = [("Add a POI",add),("Search a POI",search),("Remove a POI",delete),("Show all POIs",showall),("Add an Enquiry",enquiry),("Exit",)]
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
            current = 5
        else:
            current -= 1
        return True
    else:
        if current == 5:
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
    pass


