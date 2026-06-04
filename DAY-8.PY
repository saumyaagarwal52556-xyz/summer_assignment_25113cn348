# #half pyramid

row = int(input("Enter no of rows : "))

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")

    print()

print()

#number triangle


for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="")

    print()

print()

#character trinagle


for i in range(1,row+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")

    print()

#repeated number


for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end="")

    print()

