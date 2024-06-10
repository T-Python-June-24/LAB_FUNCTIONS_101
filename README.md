# LAB_FUNCTIONS_101


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

**Example Output for `5`**
```
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
```

#### Document the newly created function. describe what it does, then print the documentation. 


# Bonus
Rewrite the previous function so that it returns the pattern as a string, then assign the result to a variables and print it.
 '''
# LAB_FUNCTIONS_101


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

**Example Output for `5`**
```
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
```

#### Document the newly created function. describe what it does, then print the documentation. 

'''


def labSolution(rows:int):
    
    '''
    this function take an input be the type int and it store it in var 
    so i can use it in nested loop to prints the result in descending order 
    for example if the user give an input be the value 3 it will print it in the 3,2,1 
    and it Subtract the last index from the value so it will be 2,1 and so on tell the last index is 0
    but it will not print 0 
    '''
    
    for rows in range(rows,0,-1):
         for columns in range(rows,0,-1):
             print(columns, end=' ')
         print("\n")  
             
labSolution(int(input("Please enter an positve Integer : ")))
print(labSolution.__doc__)