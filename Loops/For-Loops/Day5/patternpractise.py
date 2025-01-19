"""Pattern Printing (Basic Structure):
Print patterns using stars to understand loop structure:
*
**
***   (right angled triangle....)
****

"""

#printing right angled triangle

for row in range(1,11): #if it would be solo only rows can make
    for column in range(1,row):
        print("*",end=" ") #cause if we see the row value is giving and column is iterating from 1 to that value
        #so it is kinda row is giving values in loop of column and column loop is happening in really and lastly not next line but same line
    print() #each value like  when row 5 ----> from 1 to 5 column loop iterates by putting array in same line
    #now for 6 it shouldn't print like same But on next line to make a right angled triangle...


#reverse 

for row in range(11,1,-1):
    #here 1st value will go as 11 so 11 stars will be printed in first row.. goes on decreasing to 1 as 1 can be 2 if 2value in 11,1
    for j in range(1,row):
        print("*",end="")
    print() #sep lines