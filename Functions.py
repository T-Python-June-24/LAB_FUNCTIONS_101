def Functions(num:int):

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
