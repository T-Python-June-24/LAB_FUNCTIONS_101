number=int(input("Enter any postive number : "))
def tringle_pattern(number):
    '''
    this function  takes parameter of type int that given fron user  , 
    then it prints out the result formatted in traingle patter
    '''
    for i in range(number, 0, -1):
        for j in range(i, 0, -1): # it will print each value in j starts with the i value till 0 
            print(j, end=" ")
        print()

tringle_pattern(number)
print(tringle_pattern.__doc__)