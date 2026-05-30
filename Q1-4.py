#Q1

n = int(input("Enter a number : "))
sum = 0
for i in range(n):
    sum += i
print(f"Sum of numbers are {sum}")

#Q2

num = int(input("enter a number: "))

for i in range(1,11):
    print(f"{i}*{num} = {i*num}")

#Q3

num1 = int(input("Enter a number: "))

fact=1

for i in range(1,num1):
    fact *= i

print(f"factorial of {num1} is {fact}")

#Q4
num2 = int(input("enter a number: "))
num3 = num2
digit=0

while num2 != 0 :
    digit +=1
    num2 //= 10

print(f"number of digits in {num3} is {digit}")

#end