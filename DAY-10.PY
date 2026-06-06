
number = int(input("Enter no of rows : "))

def star_pyramid(num):

    for i in range(1,num+1):

        for space in range(num-i):
            print(" ",end="")

        for star in range(1,2*i):
            print("*",end="")
        
        print()
    
    print()

def reverse_pyramid(num):
    

    for i in range(1,num+1):
        for space in range(i-1):
            print(" ",end="")

        for star in range(2*(num- i)+1):
            print("*",end="")

        

        print()

    print()


def number_pyramid(num):
    
    for i in range(1,num+1):

        for space in range(num-i):
            print(" ",end="")

        for star in range(1,i+1):
            print(star,end="")
            
        for star2 in range(i-1,0,-1):
            print(star2,end="")
        
        print()

    print()

def chracter_pyramid(num):

    for i in range(1,num+1):

        for space in range(num-i):
            print(" ",end="")

        for star in range(1,i+1):
            print(chr(64+star),end="")
            
        for star2 in range(i-1,0,-1):
            print(chr(64+star2),end="")
        
        print()

    print()


star_pyramid(number)

reverse_pyramid(number)

number_pyramid(number)

chracter_pyramid(number)