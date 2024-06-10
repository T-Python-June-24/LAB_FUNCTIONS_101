
#? def a function by the name labSolution , it takes a prameter be the type integer
def labSolution(rows:int)->int:
    '''
This function takes an integer input and prints a pattern of numbers in descending order. 
and also it starts from the input value and prints each line with numbers decreasing by 1 until reaching 1.
It continues this pattern until the last line with a single 1.
    
    '''
    
    # while rows > 0:
    for row in range(rows,0,-1):
        for column in range(rows,0,-1):  
            print(column,end=' ') 
        print("\n")
        # rows-=1  
try:   
  labSolution(int(input("Plase Enter Postive Number: ")))
except:print("\n Opss Something went wrong!!")
print(labSolution.__doc__)



def FunctionBonus(number: int) -> str:
    '''
    
    
    This function takes an int input and returns the result formatted like this:
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

# Get user input
user_input = int(input("Please enter a number: "))

# Assign the result to a variable and print it
pattern = FunctionBonus(user_input)
print(pattern)
