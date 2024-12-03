def insertionsort(numbers):
    for divider in range(len(numbers)):
        counter = divider
        while counter != 0 and numbers[counter] < numbers[counter - 1]:

            numbers[counter - 1], numbers[counter] = numbers[counter], numbers[counter - 1]
            counter = counter - 1
    return numbers
