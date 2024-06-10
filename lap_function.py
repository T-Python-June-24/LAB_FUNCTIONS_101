def pattern(parameter):
    """
    Prints a pattern of decreasing numbers starting from the given integer down to 1.
    """
    for x in range(parameter, 0, -1):
        for y in range(x, 0, -1):
            print(y, end=" ")
        print()

pattern(5)
help(pattern.__doc__)

'''## Create a function that takes 1 parameter of type int , 
then it prints out the result formatted like the following patter 
(if we give it 5 for example):

**Example Output for `5`**
```
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
#### Document the newly created function. describe what it does,
#  then print the documentation. 

'''