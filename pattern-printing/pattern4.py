n = 5  #no  of rows

for i in range(1, n+1):  # Loop controls the rows
    for j in range(1, i + 1):  #prints numbers from 1 to the current row
        print(j, end=" ")  # Prints numbers with a space on the same line
    print()  # Moves to the next line after each row