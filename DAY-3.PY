
#Q9

num = int(input("enter a number : "))
a = 0

for i in range(1,num):
    if num % i == 0:
        a +=1

if a == 1:
    print(f"The number {num} is prime")

else:
    print(f"The number {num} is not prime")
print()
# #Q10
ranges = int(input("enter a range to find prime numbers till : "))

for i in range(2,ranges+1):
    b = 0
    for j in range(2,i+1):
        if i % j == 0:
            b +=1
    if b == 1:
        print(f"{i} is prime")
    else:
        print(f"{i} is not prime")
print()
#Q11

num1 = int(input("Ener 1st number: "))
num2 = int(input("Enter 2nd number: "))

gcd = 1

for i in range(1, min(num1,num2)+1):
    if num1 %i == 0 and num2 % i == 0:
        gcd = i

print(f"GCD of {num1} and {num2} is {gcd}")
print()
#Q12

lcm = (num1*num2) // gcd
   
print(f"LCM of {num1} and {num2} is {lcm}")
print()