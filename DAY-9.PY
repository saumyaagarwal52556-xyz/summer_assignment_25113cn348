
number = int(input("enter no of rows : "))


#Reverse star pattern

def reverse_star_pattern(num):
    for i in range(num+1):
        for j in range(1,num-i+1):
            print("*",end="")

        print()

#reverse number pattern 

def reverse_number_pattern(num):
    for i in range(num+1):
        for j in range(1,num-i+1):
            print(j,end="")

        print()

#repeated character pattern

def repeated_character_pattern(num):
    for i in range(1,num):
        for j in range(1,i+1):
            print(chr(64+i),end="")

        print()
    print()

#hollow square pattern

def hollow_square_pattern(num):

    for i in range(num+1):
        for j in range(num+1):

            if i == 0 or i == num or j == 0 or j == num :
                print("*",end="")
            else:
                print(" ",end="")

        print()




reverse_star_pattern(number)

reverse_number_pattern(number)

repeated_character_pattern(number)

hollow_square_pattern(number)
