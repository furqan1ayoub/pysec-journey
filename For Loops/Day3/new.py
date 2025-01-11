
#5)Multiplication Table: Write a program to print the multiplication table of a given number using a loop.
#ans
#1) get an input 
uInput = int((input("Enter The Number To Print Mutliplication Table of --  ")))
print(f"Multiplication Table of {uInput}")
#2) use a for loop to range 10 i.e 1,11
for i in range(1,11):
    #3) just put the user input and i value and mutliply them at each step -> and print each step.....
    print(f"{uInput} x  {i} = {uInput*i}")


#6)Prime Numbers: Write a program to find all prime numbers between 1 and 101 using a loop.

for a in range(2,101):
    print("Checking ",a)
    is_Prime = True
    for i in range(2,a):
        if a % i == 0: # this is for understanding ....if a ya no ke peche values from 2 in it - it is getting divided by anyone break as it won't be prime....
            is_Prime = False
            break # cause it is divisible more than 1 and itself so -> not a prime so we don't want to check after it
        #this loop ends
    if is_Prime:print(f"{a} is a prime No.")
    else : print(f"{a} isn't a Prime No.")