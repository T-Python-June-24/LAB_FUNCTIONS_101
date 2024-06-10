def patt(x:int) -> str:
    '''This function will take a number and create a pattern for it, and store it'''
    pattern= ""
    for i in range(x,0, -1):
        for j in range(i,0, -1):
            pattern += str(j) + " "
        pattern = pattern + "\n"
    return pattern

pattern = patt(5)
print(patt.__doc__)

print(pattern)