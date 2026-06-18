
def bubble_sort(array):
    sorted_array = array.copy()
    

    for i in range(len(array)):
        for j in range(len(array) - i - 1):

            if sorted_array[j] > sorted_array[j + 1]:
                temp = sorted_array[j]
                sorted_array[j] = sorted_array[j + 1]
                sorted_array[j + 1] = temp
    

    return sorted_array

def selection_sort(array):
    sorted_array = array.copy()

    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if sorted_array[min] > sorted_array[j]:
                min = j

        temp = sorted_array[min]
        sorted_array[min] = sorted_array[i]
        sorted_array[i] = temp

    

    return sorted_array

def binary_search(array,key_value):
    sorted_array = sorted(array)

    low = 0
    high = len(sorted_array) -1

    while low <= high:

        mid = (low + high) // 2

        if sorted_array[mid] == key_value:
            return mid
        
        elif key_value < sorted_array[mid]:
            high = mid - 1

        elif key_value > sorted_array[mid]:
            low = mid + 1

    return -1

            

try:
    array_length = int(input("Enter length of array : "))
    arr = []
    

    if array_length <= 0:
        print("please input a number greater than 0.")
        exit()

    for i in range(array_length):
        arr.append(int(input("Enter a number : ")))

    print(f"sorted array using bubble sort {bubble_sort(arr)}")

    print(f"sorted array using selection sort {selection_sort(arr)}")

    target = int(input("enter a value to find index : "))

    print(f"using binary search the index of {target} is {binary_search(arr,target)}")

    desc_array = sorted(arr,reverse=True)

    print(f"array in descending order {desc_array}")



except ValueError:
    print("invalid input")   