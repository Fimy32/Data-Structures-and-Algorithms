import math

def split_list(data):
    print("Splitting",data)
    length = len(data)
    halfway = math.ceil(length/2) # ceil rounds up to nearest integer
    if length == 2:
        return (data[:halfway], data[halfway:])

def merge_list(value1, value2):
    if value1 > value2:
        return value2,value1
    else:
        return value1,value2

def mergesort(array):
    total_len = len(array)
    temp_array = array
    temp_array.append(split_list(array))
    while len(array) != total_len:
        for element in temp_array:
            temp = split_list(element)
            temp_array.remove(element)
            temp_array.append(temp)


    for element in temp_array:
        array.element = merge_list(element[0], element[1])
    return array

print(mergesort([3,8,1,9,4,5,2,7,6,0]))


