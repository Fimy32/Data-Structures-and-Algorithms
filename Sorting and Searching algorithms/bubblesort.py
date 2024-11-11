def bubblesort(numbers):
    counter = 0
    for i in range(len(numbers) - 1):
        print("\ni" + str(counter))
        for i in range(len(numbers) - i - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print(numbers)
    return numbers



sort_numbers = []
for i in range(10,0,-1):
    #sort_numbers.append(input("Enter a number:\n"))
    sort_numbers.append(i)
print(sort_numbers)
print(bubblesort(sort_numbers))