
#Recursive factorial

def factorial(a):

    if a == 0:
        return 1


    return a * factorial(a-1) 

try: 
    num = int(input("enter a number to find factorial : "))
    if num == 0:
        print("invalid number")

    else:
        print(f"factorial of {num} is {factorial(num)}")

except ValueError:
    print("invalid input")


#Recusive fibonacci

def fibonacci(b):

    if b == 0 or b == 1:
        return b
    
    return fibonacci(b-1) + fibonacci(b-2)

try :
    number = int(input("enter a number to print fibonacci series : "))
    print("Fibonacci series : ")
    
    if number <= 0:
        print("please enter a positive number")

    else:
        for i in range(number):
            print(i,fibonacci(i))

except ValueError:
    print("invalid input")

#Recursive sum of digits

def sum_of_digits(c):
    if c < 10:
        return c


    return (c % 10) + sum_of_digits(c // 10)
    
num1 = int(input("Enter a number : "))
print(sum_of_digits(num1))

#Recursive reverse number

def reverse_number(d):
    ela = len(str(d))

    if d < 10:
        return d
    
    ela -=1

    return ((d % 10) * (10 ** ela)) + reverse_number(d // 10)

try:
    num = int(input("Enter a number to find reverse number : "))
    
    sign=-1 if num < 0 else 1


    print(sign*reverse_number(abs(num)))

except ValueError:
    print("invalid input")

