
# defining the function 
def print_numbers (n:int):
  '''
  This function takes integer parameter and prints the a pattern of the number decremently 
  '''
  for i in range(n, 0, -1):
    for j in range(i, 0, -1):
      print(j, end=" ")
    # for printing a new line 
    print("")

# printing the function documentation
print(print_numbers.__doc__)

# Calling the function
print_numbers(5)