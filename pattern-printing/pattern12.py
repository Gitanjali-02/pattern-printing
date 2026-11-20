n = 5  # Number of rows
# upper half of the butterfly pattern
for i in range(1, n + 1):  # controls the rows of the upper half
    for j in range(i):  # prints increasing stars on the left side
        print("*", end=" ")
    for j in range(2 * (n - i)):  # prints decreasing middle spaces
        print(" ", end=" ")
    for j in range(i):  # prints increasing stars on the right side
        print("*", end=" ")
    print()  # moves to the next line

# Lower half of the butterfly pattern
for i in range(n - 1, 0, -1):  # controls the rows of the lower half
    for j in range(i):  # prints decreasing stars on the left side
        print("*", end=" ")
    for j in range(2 * (n - i)):  # prints increasing middle spaces
        print(" ", end=" ")
    for j in range(i):  # prints decreasing stars on the right side
        print("*", end=" ")
    print()  # moves to the next line