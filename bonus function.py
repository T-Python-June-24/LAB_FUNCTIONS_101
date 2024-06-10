def function(num:int):
    """
    Prints a pattern of decreasing numbers starting from the given integer down to 1.
    """
    result='-'
    for x in range(num, 0, -1):
        for y in range(x, 0, -1):
         result += str(y)
         result += '\n'

        
        return result


pattern = function() 
print(pattern) 







'''Bonus
Rewrite the previous function so that it returns the pattern as a string, 
then assign the result to a variables and print it.
'''