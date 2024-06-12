def Functions(num:int):
    '''This is the functions lap solution
    
    please be aware that Abdullah Aldhamen solved it
    
    after 2 hours of work'''

    for i in range(num, 0, -1):
        rowNums = []
  
        for j in range(1, i + 1):
            rowNums.append(j)
  
        rowNums.reverse()
  
        for n in rowNums:
            print(n, end=" ")
  
        print()

    return ""

Functions(5)
print(Functions.__doc__)