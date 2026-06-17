
def merge_array(array1,array2):
    set1 = set(array1)
    set2 = set(array2)
    set1.update(set2)

    new_array = list(set1)

    return new_array

def union_array(array1,array2):

    set1 = set(array1)
    set2 = set(array2)

    new_set = set1 | set2

    new_array = list(new_set)

    return new_array

def intersection_array(array1,array2):
    
    set1 = set(array1)
    set2 = set(array2)

    return (list(set1 & set2))

try:
    array_length = int(input("Enter length of array : "))
    arr = []
    second_array = []

    if array_length <= 0:
        print("please input a number greater than 0.")
        exit()

    for i in range(array_length):
        arr.append(int(input("Enter a number : ")))

    
    for i in range(array_length):
        second_array.append(int(input("Enter a number : ")))

    print(f"merged array is {merge_array(arr,second_array)}")

    print(f"union of array {union_array(arr,second_array)}")

    print(f"intersection of array {intersection_array(arr,second_array)}")

    print(f"common elements are {intersection_array(arr,second_array)}")



except ValueError:
    print("invalid input")