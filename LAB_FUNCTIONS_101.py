def reverse_num(x:int):
    for i in range(x, 0, -1):
        for n in range(i, 0, -1):
            print(f"{n} ", end="")
        print("")
reverse_num(int(input("Enter an integer: ")))