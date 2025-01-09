#3)Odd Numbers: Write a program to print all odd numbers from 1 to 75 using a loop.
#ans: (easy)

for i in range(1,76):
    if(i%2 !=0):
        print(i,"- odd number..")
    else:
        print(i,"-even number...")
#simple:- i iterates from 1 to 75 over every number & if on each loop step 
# if i value is divisble by 2 -> even and if not -> odd





#4)Factorial: Write a program to calculate the factorial of a number using a loop.
#answ

#s1: get the no from user
inputUser = int(input("Enter the no. to find a factorial of - "))

#s2: set the box(#initializing factorial box) value where we multiply any value incoming :-
factorial = 1 
#s3: use for loop from 1 upto that input NO.  -> using range

for i in range(1,inputUser+1): #cause -> last here skipped so we add 1 to not skip the inputUser but include it too
    print(i) # better understanding in terminal
    
    factorial*=i #mutliplying step->(see md file to get it s4)
    
    #it keep on looping /repeating until inputUser reaches 
    
    #at last when it reaches inputUser Breaks 

#s5:now we got value print it
print(f"The Factorial of {inputUser} is - {factorial} ;")  