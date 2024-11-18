from hashtable.hashtable import HashTable

current = 0
POI_Hashtable = HashTable()

def menu():
    options = [("Add a POI",add),("Show all POIs",search),("Show all POIs",showall),("Remove a POI",delete),("Add an Enquiry",enquiry),("Exit",)]
    for i in range(len(options) - 1):
        print(options[i][0], end=" ")
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
    POI_Hashtable.add(input("Please Enter POI Name"),(input("Please Enter POI type"),input("Please Enter POI Desc")))

def search():
    pass

def showall():
    pass

def delete():
    pass

def enquiry():
    pass


