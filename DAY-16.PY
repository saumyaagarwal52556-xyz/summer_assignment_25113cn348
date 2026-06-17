
def missing_number(arr):

    largest_number = max(arr)
    smallest_number = min(arr)

    all_numbers = set(range(smallest_number,largest_number+1))

    missing_numbers = list(all_numbers - set(arr))

    print(f"missing numbers are : {missing_numbers}")



def frequency(array):

    freq_dict = {}

    if not array:
        print("empty array.")
        return

    for num in array :
        if num in freq_dict:
            freq_dict[num] += 1

        else:
            freq_dict[num] = 1

    max_freq = max(freq_dict.values())
    max_freq_key = [k for k, v in freq_dict.items() if v == max_freq]

    if len(max_freq_key) == 1:
        print(f"maximum frequence element {max_freq_key[0]} occurs {max_freq} times")

    else:
        print(f"Multiple elements tied for maximum frequency ({max_freq} times): {max_freq_key}")



def pair_with_sum(array,sum_number):

    seen = set()

    for number in array:
        target = sum_number - number

        if target in seen:
            print(target,number)

        seen.add(number)



def duplicates(array):
    seen = set()
    duplicates_value = set()

    for num in array:
        if num in seen:
            duplicates_value.add(num)

        seen.add(num)

    print(f"updated array is {seen}")

    print(f"duplicates are {duplicates_value}")


            

try:

    
    array_length = int(input("Enter length of array : "))
    arr=[]

    if array_length <= 0:
        print("please input a number greater than 0.")
        exit()

    for i in range(array_length):
        arr.append(int(input("Enter a number : ")))


    missing_number(arr)

    frequency(arr)

    #find pair with given sum

    target_sum = int(input("Enter a sum : "))

    pair_with_sum(arr,target_sum)

    duplicates(arr)



except ValueError:
    print("invalid input")