def insertionsort(numbers):
    for divider in range(len(numbers)):
        print(numbers, "Divider:",numbers[divider][0])
        counter = divider
        while counter != 0 and numbers[counter] < numbers[counter - 1]:

            numbers[counter - 1], numbers[counter] = numbers[counter], numbers[counter - 1]
            counter = counter - 1
        print("Inserting",numbers[counter])
    return numbers
