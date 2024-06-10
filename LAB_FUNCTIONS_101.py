def reverse_num(x:int):
    '''Takes an integer and prints a pattern'''
    for i in range(x, 0, -1):
        for n in range(i, 0, -1):
            print(f"{n} ", end="")
        print("")
reverse_num(int(input("Enter an integer: ")))
print(reverse_num.__doc__)