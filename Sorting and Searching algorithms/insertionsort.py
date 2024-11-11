import random

def insertionsort(numbers):
    for divider in range(len(numbers)):
        print(numbers, "Divider:",numbers[divider])
        counter = divider
        while counter != 0 and numbers[counter] < numbers[counter - 1]:

            numbers[counter - 1], numbers[counter] = numbers[counter], numbers[counter - 1]
            counter = counter - 1
        print("Inserting",numbers[counter])
    return numbers


sort_numbers = []
for i in range(10,0,-1):
    #sort_numbers.append(input("Enter a number:\n"))
    sort_numbers.append(i)
    #sort_numbers.append(random.randint(0,20))

print(insertionsort(sort_numbers))
