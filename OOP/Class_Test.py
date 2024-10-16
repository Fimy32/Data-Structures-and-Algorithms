from operator import truediv


class Cat:

    def __init__(self, name, weight, colour, evilness):
        self.name = name
        self.weight = weight
        self.colour = colour
        self.evilness = int(evilness)

    # def __init__(self, name, weight):
    #     self.name = name
    #     self.weight = weight

    def eat(self):
        self.weight += 1

    def eat(self, amount):
        self.weight += amount

    def return_attributes(self):
        return self.name, self.weight, self.colour, self.evilness

    def walk(self):
        if self.weight < 1:
            self.weight -= 1

class Student:
    def __init__(self, id, name, course, mark):
        self.id = id
        self.name = name
        self.course = course
        self.mark = int(mark)

    def return_attributes(self):
        return self.id, self.name, self.course, self.mark

    def setMark(self):
        if self.mark > -1 and self.mark < 101:
            return True
        else:
            return False

    def printGrade(self):
        if self.mark > 69:
            print("First")
        elif self.mark > 59:
            print("2/1")
        elif self.mark > 49:
            print("2/2")
        elif self.mark > 39:
            print("Third")
        else:
            print("Fail")
        print("\n")