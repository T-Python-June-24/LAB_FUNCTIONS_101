user_choice = int(input("Enter a number: "))

def write_in_sequence(num):
    """
    This function is taking a number which usually comes from the user, 
    the given parameter will be stored in a temporary variable, to keep track the range of the numbers
    so while the temporary value is bigger than 0, we loop through a range of the current_iteration to 0 decrementing it,
    for example, if the user entered 5, the current_iteration will become 5 and the for loop is adding from the range of 5
    to that string, then it will be decremented, and become 4, and the loop will start again but with value of 4, and with that till 
    it becomes 0, so the current iteration is the controller, and when each iteration ended, we add a "\n" to skip to the next line 
    """
    current_iteration = num #we set it temporarily because we want to decrement it with each loop
    temporary_string = "" #we set it to empty string, to fill it with the iterations
    
    while current_iteration > 0: #add stop point where the loop should stops when current_iteration equals to 0
        
        for number in range(current_iteration, 0, -1): #we loops from current iteration to 0, it could be 5, 4, 3, 2, 1 ...etc
            temporary_string += str(number) + " " #we convert the number to string and add it to temporary_string
                        
        temporary_string += "\n" #if an iteration ended, like 54321 or 4321, we add this to seperate the lines
        current_iteration -= 1 #we decrement the current iteration to control the loop
    print(temporary_string)
    
    
def write_in_sequence2(num) -> str:
    """
    This function is taking a number which usually comes from the user, 
    the given parameter will be stored in a temporary variable, to keep track the range of the numbers
    so while the temporary value is bigger than 0, we loop through a range of the current_iteration to 0 decrementing it,
    for example, if the user entered 5, the current_iteration will become 5 and the for loop is adding from the range of 5
    to that string, then it will be decremented, and become 4, and the loop will start again but with value of 4, and with that till 
    it becomes 0, so the current iteration is the controller, and when each iteration ended, we add a "\n" to skip to the next line 

    """
    current_iteration = num 
    temporary_string = ""
    
    while current_iteration > 0:
        
        for number in range(current_iteration, 0, -1):
            temporary_string += str(number) + " "
                        
        temporary_string += "\n"
        current_iteration -= 1
    return temporary_string


# first problem
write_in_sequence(user_choice)
print(write_in_sequence.__doc__)
print("-"*20)

# bonus problem
result = write_in_sequence2(user_choice)
print(result)
print(write_in_sequence2.__doc__)
print(type(write_in_sequence2(user_choice)))