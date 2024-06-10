def patt(x:int):
    '''This function will take a number and create a pattern for it'''
    for i in range(x,0, -1):
        for j in range(i,0, -1):
            print(j, end=" ")
        print()

patt(5)
print(patt.__doc__)
