try : 
    num = int(input("Enter length of array : "))
    
    arr =[]

    if num == 0:
        print("please enter number greater than 0")

    #input array


    for i in range(num):
        c = int(input("enter a number :"))
        arr.append(c)

    #print array
    
    print("array numbers are : ")

    for i in range(num):
        print(arr[i])

    #sum of array

    sum = 0
    for i in range(num):
        sum += arr[i]

    #average of array

    average = sum // num

    print(f"sum of array is {sum}")

    print(f"\navearge of array is {average}")

    #largest and smallest number 

    max_val = arr[0]
    min_val = arr[0]

    for i in range(num):
        if arr[i] > max_val :
            max_val = arr[i]

        if arr[i] < min_val:
            min_val = arr[i]

    print(f"maximum number is {max_val} and minimum number is {min_val}")

    #alternate method
    print(f"maximum number is {max(arr)} and minimum number is {min(arr)}")

    even_count = 0
    odd_count = 0

    for i in range(num):
        if arr[i] % 2 == 0:
            even_count +=1

        else:
            odd_count += 1

    print(f"even count is {even_count} and odd count is {odd_count}")


except ValueError:
    print("invalid number ")