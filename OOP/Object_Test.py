from Class_Test import Cat
import random

# cat1 = Cat("Binnie", 4)
# cat2 = Cat("Clyde", 2)
# cat1.eat(random.randint(1,5))
# cat2.eat(random.randint(1,5))
# print(cat1.name, cat1.weight)
# print(cat2.name, cat2.weight)
#
cat1 = Cat("Flathead", 4,"purple",15)
cat2 = Cat("Cupra", 3,"orange",6)
cat3 = Cat("Old_Tom",6,"green",10)

print(cat1.return_attributes(),cat2.return_attributes(),cat3.return_attributes())

cat3.eat(1)
cat1.walk()
cat2.walk()
cat3.walk()

print(cat1.return_attributes(),cat2.return_attributes(),cat3.return_attributes())