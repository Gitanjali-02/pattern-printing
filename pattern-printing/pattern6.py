n=5   #no of rows
for i in range(1,n+1):    #loop for rows
    for j in range(n-i):   #loop for print spaces
        print(" ",end=" ")   #print spaces
    for k in range(i):    #loop for print star
        print("*",end=" ")   #print star with space
    print()    #move to next line
