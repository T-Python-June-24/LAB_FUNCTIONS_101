def pyramidShape (n:int ):
    ''' This function print revers  left pyramid of numbers '''

    for i in range(n,0, -1  ):
        for j in range( i, 0, -1):
            print(j, end=" ")
    return("")

pyramidShape(5)
print(pyramidShape.__doc__)


