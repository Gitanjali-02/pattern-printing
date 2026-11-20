
n = 5   #no of rows and columns
for i in range(n):    #loop for rows
    for j in range(n):    #loop for column
        if i == 0 or i == n-1 or j == 0 or j == n-1:   # print stars on boundry
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print spaces inside
    print()  # Move to next line