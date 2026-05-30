
num = int(input("enter a number: "))
num1 = num
sum = 0
rev = 0
product = 1

while num != 0 :
    r = num % 10
    sum += r
    rev = rev * 10 + r
    product = product * r
    num //= 10

print(f"sum of digits of {num1} is {sum}")

print(f"the reverse of number {num1} is {rev}")

print(f"the product of number {num1} is {product}")

if num1 == rev :
    print(f"the number {num1} is palindrome")

else:
    print("not a palindrome")

#end