
def printPattren(x:int)->int:
    ''' this method take an intger and print the result in decreasing format'''
    for i in range(x,0,-1):
        for j in range(i,0,-1):  
            print(j,end=' ')
        print()



printPattren(5)
print(printPattren.__doc__) #printing the documantion of printPattren method.