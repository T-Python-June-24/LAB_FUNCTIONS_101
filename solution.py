'''
# LAB_FUNCTIONS_101


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following pattern (if we give it 5 for example):

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

def LabSolution(rows:int)->int:
    '''
  this is were the doc should be
     '''
    for row in range(rows,0,-1):
        for column in range(row,0,-1):
            print(column,end=" ")
        print("\n")
            
           
LabSolution(int(input("Plase enter a postive number: ")))
print(LabSolution.__doc__)
    