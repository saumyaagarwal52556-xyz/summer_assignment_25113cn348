
def linear_search(arr,target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

def frequency(arr):

    freq_dict = {}
    
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1

        else:
            freq_dict[num] = 1

    return freq_dict

def second_largest(arr):
    
    sorted_arr = sorted(arr,reverse=True)
    
    for i in range(len(arr) -1 ):
        if sorted_arr[i] != sorted_arr[i+1]:
            print(f"second largest element is {sorted_arr[i+1]}\n")
            return
        
    print("no second largest found \n")

def duplicates(arr):
    
    seen = set()
    dup_element = set()

    for num in arr :
        if num in seen :
            dup_element.add(num)

        else:
            seen.add(num)

    return len(dup_element)
                            


try :
    num = int(input("Enter length of array: "))
    arr = []
    target = int(input("Enter a target : "))

    for i in range(num):
        arr.append(int(input("Enter a number : ")))

    print(linear_search(arr,target))
    
    #frequency of element

    frq1 = frequency(arr)

    for number,count in frq1.items():
       print(f"{number}       {count}")

    #second largest element

    second_largest(arr)

    #duplicats in array 

    print(f"no of duplicates are {duplicates(arr)}\n")


    

except ValueError:
    print("invalid input")