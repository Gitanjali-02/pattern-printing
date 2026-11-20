n=5  #no of rows

for i in range(1,n+1):  #loop controls the rows
    for j in range(n - i):  #prints spaces before stars to create a pyramid shape
        print(" ", end=" ")  #prints spaces on the same line
    for k in range(2 * i - 1):  #prints odd numbers of stars in each row
        print("*", end=" ")  #prints stars with spaces between them
    print()  #moves to the next line