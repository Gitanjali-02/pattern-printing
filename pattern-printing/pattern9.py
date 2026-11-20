
n = 5  # Number of rows
# Upper half of the diamond
for i in range(1, n + 1):  # controls the rows
    for j in range(n - i):  #prints spaces before stars
        print(" ", end=" ")
    for k in range(2 * i - 1):  # Prints odd numbers of stars
        print("*", end=" ")
    print()  # Moves to the next line

# Lower half of the diamond
for i in range(n - 1, 0, -1):  # Controls the rows in reverse order
    for j in range(n - i):  # Prints spaces before stars
        print(" ", end=" ")
    for k in range(2 * i - 1):  # Prints decreasing stars
        print("*", end=" ")
    print()  # Moves to the next line
