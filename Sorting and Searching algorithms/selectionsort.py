import random

def selectionsort(numbers):
    for i in range(len(numbers) - 1):
        temp = i
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j] and numbers[j] < numbers[temp]:
                temp = j
        numbers[i], numbers[temp] = numbers[temp], numbers[i]
        print(numbers)
    return numbers



sort_numbers = []
for i in range(10,0,-1):
    #sort_numbers.append(input("Enter a number:\n"))
    #sort_numbers.append(i)
    sort_numbers.append(random.randint(0,20))
print(sort_numbers)
print(selectionsort(sort_numbers))
