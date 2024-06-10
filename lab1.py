def takes(number:int):
    '''
    A function that takes a single parameter of type int, then prints the result in the following format (if we give it 5 for example):

**Example output of `5`**
```
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
```````````````
    '''
    for num in range(number,0,-1):
        for num1 in range(num , 0 ,-1):
            print(num1 , end=" ")
        print()
print(takes.__doc__)    
takes(5)

