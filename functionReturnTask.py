n = int(input("Enter an integer number: "))

def getPattern(n):
    '''This function takes an integer number n from the user then return a string containing the numbers shape. It concatenates numbers n to 1 in the first line then concatenates n-1 to 1 in the second line, etc.'''
    str = ""
    for i in range(n , 0,-1):
        for j in range (i,0,-1):
            str += f"{j}" + " "
        str += "\n"
    return str

string = getPattern(n)
print(string)
print(getPattern.__doc__)