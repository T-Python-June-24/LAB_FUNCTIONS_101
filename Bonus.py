
def printPattren(x:int)->int:
    ''' this method take an intger and return the result in decreasing format'''
    y=""
    for i in range(x,0,-1):
        for j in range(i,0,-1):
            y+=str(j)+" "
            
        y+='\n'
    return y



print(printPattren(5))
print(printPattren.__doc__)