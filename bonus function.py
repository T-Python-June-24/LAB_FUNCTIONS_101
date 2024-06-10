def pattern(parameter):
    """
    Prints a pattern of decreasing numbers starting from the given integer down to 1.
    """
    for x in range(parameter, 0, -1):
        for y in range(x, 0, -1):
            print(y, end=" ")
        print()










'''Bonus
Rewrite the previous function so that it returns the pattern as a string, 
then assign the result to a variables and print it.
'''