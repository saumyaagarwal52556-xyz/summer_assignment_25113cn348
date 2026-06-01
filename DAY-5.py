
#to check perfect number

def perfectnumber(num):
    if num == 0:
        return False

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
    if num1 < 0:
        return False

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

#print factors 

def factor(number):
    print(f"factors of {number} are :")

    factor_list = []

    for i in range(1,number+1):

        if number % i == 0:
            factor_list.append(str(i))

    print(",".join(factor_list))

num = int(input("Enter a number to print factors: "))

factor(num)


# largest prime factors

def primenumber(a):

    c = 0

    for p in range(1,a):
        if a % p == 0:
            c += 1

    if c == 1:
        return True
    
    else:
        return False
    
def largest_factor(num):

    prime_factor = 0

    for i in range(1,num+1):

        if num % i == 0 :
            if primenumber(i):
                prime_factor = i

    print(f"largest prime factor of {num} is {prime_factor}")

number = int(input("Enter a number to find prime factor: "))

largest_factor(number)