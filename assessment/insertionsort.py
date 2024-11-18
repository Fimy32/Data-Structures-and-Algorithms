def insertionsort(numbers):
    temp = []
    
    for element in numbers:
        temp2 = ""
        for char in element:
            temp2 = temp2 + ord(char)
        temp.append(temp2)
    for divider in range(len(numbers)):
        #print(numbers, "Divider:",numbers[divider])
        counter = divider
        while counter != 0 and numbers[counter] < numbers[counter - 1]:

            numbers[counter - 1], numbers[counter] = numbers[counter], numbers[counter - 1]
            counter = counter - 1
        #print("Inserting",numbers[counter])
        numbers = [chr(value) for value in temp]
    return numbers
