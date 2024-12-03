correct_sort = []

def quicksort(arr):
    global correct_sort
    for item in arr:
        correct_sort.append(item)
    correct_sort.sort()
    print(correct_sort)
    inner_quicksort(arr, 0, len(arr)-1)

def inner_quicksort(array,start,end):
    #if array[start] < array[end]:
    print(array)
    if array == correct_sort:
        print("Sorted")
        return array
    else:
        inner_quicksort(array,start,partition(array,start,end))
   # else:
        #array[start],array[end] = array[end],array[start]


def partition(array,start,end):
    pivot = array[(start+end)//2]
    i = start
    j = end
    while array[i] < pivot:
        i += 1
    while array[j] > pivot:
        j -= 1
    if i != j:
        array[i], array[j] = array[j], array[i]
    else:
        pass
    inner_quicksort(array,0,len(array)-1)


print(quicksort([9,2,4,3,8,6,7,1,5]))

print(quicksort([9,8,7,6,5,4,3,2,1]))
