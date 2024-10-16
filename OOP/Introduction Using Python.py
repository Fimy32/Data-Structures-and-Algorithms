class Cat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 1



Super_Cat = Cat('Bob', 5)

Super_Cat.eat()

print(Super_Cat.weight)