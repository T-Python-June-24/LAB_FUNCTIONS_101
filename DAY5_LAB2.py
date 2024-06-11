# ## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter 
# (if we give it 5 for example):

# **Example Output for `5`**
# ```
# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   
# ```

# #### Document the newly created function. describe what it does, then print the documentation. 



def func1(x:int):
    '''    
    This function printing a pattern of numbers in descending order starting from the given integer.
    
    :param x: An integer that defines the starting point of the pattern
    '''
    for i in range(x, 0, -1):
        for j in range(i, 0, -1):
            print(j, end = ' ')
        print()


print()
func1(5)

print()
print(func1.__doc__)



print(f"\n\n\n", "_"*25, "\n\n\n")

# # Bonus
# Rewrite the previous function so that it returns the pattern as a string, then assign the result to a variables and print it.

def func2(x:int) -> str:
    '''    
    This function printing a pattern of numbers in descending order starting from the given integer and returns it as a string.
    
    :param x: An integer that defines the starting point of the pattern
    :return: The pattern in string format
    '''

    patt = ""

    for i in range(x, 0, -1):
        for j in range(i, 0, -1):
            patt += str(j) + " "
        patt += "\n"
    return patt

pattern = func2(5)

print(pattern)
