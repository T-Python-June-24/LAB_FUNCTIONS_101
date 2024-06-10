n = int(input("Enter an integer number: "))

def print_Numbers(n):
    '''This function takes an integer number n from the user then prints the numbers n to 1 in a triangle shape. It prints n to 1 in the first line then prints n-1 to 1 in the second line, etc.'''
    for i in range(n , 0,-1):
        for j in range (i,0,-1):
            print(j,end=" ")
        print(end="\n")


print_Numbers(n)
print(print_Numbers.__doc__)