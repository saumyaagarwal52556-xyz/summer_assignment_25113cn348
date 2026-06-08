
def palindrome(num):
    num1 = num
    rev = 0

    while num1 != 0:
        r = num1 % 10
        rev = rev * 10 + r
        num1 //= 10

    if rev == num :
        return True
    
    else:
        return False
    

num = int(input("Enter number to check palindrome or not : "))

if palindrome(num):
    print(f"{num} is palindrome")

else:
    print(f"{num} is not palindrome ")


def armstrong(number):

    length = len(str(number))
    
    num1 = number
    digit = 0
    sum = 0
    while number != 0:
        digit = number % 10
        sum = sum + digit ** length
        number //= 10
    
    if num1 == sum:
        return True

    else :
        return False
        

number = int(input("Enter a number to check if it is armstrong or not : "))
if armstrong(number):
    print(f"the number {number} is armstrong number")

else:
    print(f"the number {number} is not an armstrong number")




def fibonacci(a):
    firstnum = 0
    secondnum = 1

    for i in range(a):
        print(firstnum,end=" ")
        thirdnum = secondnum + firstnum
        firstnum = secondnum
        secondnum = thirdnum

    print()

num = int(input("Enter a number to print fibonacci: "))
fibonacci(num)




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
