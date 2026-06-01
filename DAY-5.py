
#to check perfect number

def perfectnumber(num):

    factor = 0
    for i in range(1,num):
        if num % i == 0 :
            factor = factor + i

    if factor == num :
        return True
    else:
        return False
    
number = int(input("Enter number to check whether a perfect or not : "))

if perfectnumber(number):
    print(f"the number {number} is a perfect number")

else:
    print(f"the number {number} is not a perfect number")

#strong number

def factorial(fac):
    rem = 1

    for i in range(1,fac+1):
        rem = rem*i

    return rem

def strong_number(num1):

    last_digit = 0
    total_sum = 0
    num2 = num1

    while num1 != 0:

        last_digit = num1 % 10
        total_sum = total_sum +factorial(last_digit)

        num1 //= 10

    if num2 == total_sum :
        return True
    else:
        return False

number_strong = int(input("Enter a number to check it is strong or not : "))

if strong_number(number_strong):
    print(f"the number {number_strong} is strong number")

else :
    print(f"the number {number_strong} is not strong number")