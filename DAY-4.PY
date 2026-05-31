
#to generate nad find nth fibonacci series

def fibonacci(a):
    firstnum = 0
    secondnum = 1

    for i in range(a):
        print(firstnum,end=" ")
        thirdnum = secondnum + firstnum
        firstnum = secondnum
        secondnum = thirdnum

num = int(input("Enter a number: "))
fibonacci(num)

#to check armstrong number

def armstrong(number):
    
    num1 = number
    digit = 0
    sum = 0
    while number != 0:
        digit = number % 10
        sum = sum + digit*digit*digit
        number //= 10
    
    if num1 == sum:
        return True

    else :
        return False
        

number = int(input("Enter a number to check if it is armstrong or not : "))
if armstrong(number):
    print(f"the number {number} is armstong number")

else:
    print(f"the number {number} is not an armstrong number")


#to find nth armstrong number

ranges = int(input("Enter a range till which to find armstrong number : "))

for i in range(1,ranges+1):
    if armstrong(i):
        print(f"the number {i} is armstong number")

    