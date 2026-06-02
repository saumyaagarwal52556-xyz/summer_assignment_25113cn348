#decimal to binary

try:
    num = int(input("Enter a number to convert decimal to binary: "))
    
    num1 = num
    num_list = []

    while num1 != 0:
        num_list.append(str(num1 % 2))

        num1 //= 2

    num_list.reverse()

    print("".join(num_list))
    
    #alternate method

    print(bin(num)[2:])

except ValueError:
    print("invalid number")

print()


#binary to decimal

try :
    binary_number = int(input("Enter a binary number: "))

    bn = binary_number
    a=0
    decimal_number = 0

    while bn != 0:
        
        ld = bn % 10
        decimal_number = decimal_number + ld * (2**a)
        a += 1

    print(f"binary number {binary_number} into decimal {decimal_number}")


except ValueError:
    print("invaild number")

#count set bits in a number

def count_set_bits(num):
    return bin(num).count("1")

    # Alternate method

    # num_binary = str(bin(num)[2:])
    # count = 0

    # for char in num_binary:
    #     if char == "1":
    #         count += 1 

    # return count

num = int(input("Enter a number to count set bits : "))

print(f"Binary form of {num} is {bin(num)[2:]}")
print(f"No of set bits in {num} : {count_set_bits(num)}")

# find x^n

try :
    
    number = int(input("Enter a number : "))
    power = int(input("Enter a power: "))
    result = 1

    if power == 0:
        result = 1

    for i in range(1,power+1): 

        result = result*number
    
    if power < 0 :
        result = 1 / result

    print(f" {number}^{power} = {result}")

except ValueError:
    print("invalid number")
