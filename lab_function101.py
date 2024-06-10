def numbers_pattern(number:int): # void function does not return value 
    
    '''
        the function takes 1 parameter of type int 
        then it prints out the result formatted in a pattern
    '''

    for i in range(number,0,-1): # outer 'for loop'  
        
        for j in range(i, 0, -1): # inner 'for loop'
            print(j, end=" ") # change end = " " to print j in one row for this i 
        print() # to print new line for the second i 

numbers_pattern(int(input("Enter a number to see pattern : ")))
print("\n Below is the document of numbers_pattern function ")
print("-"*100)
print(numbers_pattern.__doc__) # to print document of numbers_pattern function 
print("-"*100)


