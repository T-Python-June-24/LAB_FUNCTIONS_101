def pattern(parameter):
    for i in range(parameter, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

pattern(5)


####Description: nested for loop
# first loop focuses on the numbers in order by column (going down)
# the second loop focuses on doing the same exact thing but by row (from side to side)
