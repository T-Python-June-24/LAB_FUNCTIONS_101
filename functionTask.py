n = int(input("Enter an integer number: "))

def print_Numbers(n):
    for i in range(n , 0,-1):
        for j in range (i,0,-1):
            print(j,end=" ")
        print(end="\n")


print_Numbers(n)