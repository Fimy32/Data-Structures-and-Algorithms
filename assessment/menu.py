current = 0
def menu():
    print("HellO")
    options = [("Add a POI",add),("Remove a POI",delete),("Add an Enquiry",enquiry),("Exit",)]
    option = input("Would you like to " + options[current][0] + "? (Y/N)")
    if option == "Y" and options[current][0] == "Exit":
        return False
    elif option == "Y":
        options[current][1]()
        return True
    else:
        current += 1
        return True
    


def add():
    print("add")

def delete():
    pass

def enquiry():
    pass