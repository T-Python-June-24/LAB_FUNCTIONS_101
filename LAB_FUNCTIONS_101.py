number=int(input("Enter any postive number : "))
def tringle_pattern(number):
 
     for i in range(number, 0, -1):
        for j in range(i, 0, -1): # it will print each value in j starts with the i value till 0 
            print(j, end=" ")
        print()

tringle_pattern(number)