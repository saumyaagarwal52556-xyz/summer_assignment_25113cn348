
def sum(a,b):
    return a+b

def maximum_number(c,d):
    return c if c>d else d

def prime_number(a):

    b = 0

    for i in range(2,a):
        if a % i == 0:
            b +=1

    if b == 0:
        return True

    else:
        return False

def factorial(num):

    if num == 0 or num == 1:
        return 1

    return num*factorial(num-1)

try:
    number = int(input("Enter 1st number to find sum : "))
    
    number2 = int(input("Enter 2nd number to find sum : "))
    
    print(f"sum of {number} and {number2} is {sum(number,number2)}")

    
    print(f"maximum number is {maximum_number(number,number2)}")

    number3 = int(input("Enter number to find prime  : "))

    number4 = int(input("Enter number to find factorial  : "))


    if prime_number(number3):
        print(f"{number3} is prime")

    else:
        print(f"{number3} is not prime")


    print(f"factorial of {number4} is {factorial(number4)}")

except ValueError:
    print("invalid input")