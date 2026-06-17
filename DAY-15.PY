
def reverse_arr(array):
     
    org_array = array.copy()

    length = len(org_array)

    for num in range(length // 2):
        temp = org_array[num]
        org_array[num] = org_array[(length - num - 1)]
        org_array[(length - num - 1)] = temp

    return array

def rotate_left(array):
    position = int(input("enter a postion to rotate array left : "))

    position = position % len(array)

    return array[position:] + array[:position]

def rotate_right(array):
    position = int(input("enter a postion to rotate array right : "))

    position = position % len(array)

    return array[-position:] + array[:-position]

def zeros_to_end(array):

    org_array = array.copy()

    new_array = []

    for num in array [:] :
        if num == 0:
            org_array.remove(num)
            new_array.append(num)

    return org_array + new_array


try:
    num = int(input("Enter length of array : "))

    arr = []

    if num == 0:
        print("please enter a number greater than 0.")


    for i in range(num):
        arr.append(int(input("Enter a number : ")))

    print(f"\noriginal array is {arr}\n")

    #reversed array

    print(f"reversed array is {reverse_arr(arr)}\n")

    #rotate left

    print(f"array rotated left is {rotate_left(arr)}\n")

    #rotate right

    print(f"array rotated right is {rotate_right(arr)}\n")

    print(f"zeors at end = {zeros_to_end(arr)}\n")


except ValueError:
    print("invalid input")