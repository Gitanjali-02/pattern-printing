n=5     #no of rows
for i in range(1,n+1): # loop for rows
    for j in range(i):  #loop for printing stars
        if i==1 or i==n or j==0 or j==i-1:    #logic for printing stars on boundry
            print("*",end=" ")    #prints star 
        else:
            print(" ",end=" ")    #print spaces
    print()  # move to next line