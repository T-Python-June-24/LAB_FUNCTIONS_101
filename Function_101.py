def FunctionLab(number:int) -> int: #the return type should be a string -> str
    '''
    this funtion takes an int input then it prints out the result formatted like this
    5 4 3 2 1   
    4 3 2 1   
    3 2 1   
    2 1   
    1  
    
    it takes the the user number as input like 5 then i toke the number into nested loop 
    the first loop tells the count the number of row and the second one count the number of colmuns
    
    '''
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()

        
FunctionLab(int(input("plase enter a number ")))


def FunctionBonus(number:int): #the return type should be a string -> str 
    '''
    this function takes an int input then it returns the result formatted like this
    5 4 3 2 1   
    4 3 2 1   
    3 2 1   
    2 1   
    1  
    '''
    result = ''
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + ' '
        result += '\n'
    return result

pattern = FunctionBonus() #! assign the result to a variable
print(pattern) #!print the variabel 