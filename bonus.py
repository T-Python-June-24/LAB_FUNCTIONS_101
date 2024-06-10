def numbers_pattern(number:int)-> str:
    pattern:str = "" # for store the pattren of the number in it 
    for i in range(number,0,-1):
        
        for j in range(i, 0, -1):
            pattern = pattern + " " + str(j) # concatenation of string 
        pattern += "\n" 

    return pattern 

numbers_pattern_string = numbers_pattern(3)
print(numbers_pattern_string)