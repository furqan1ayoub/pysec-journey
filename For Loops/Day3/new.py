
#5)Multiplication Table: Write a program to print the multiplication table of a given number using a loop.
#ans
#1) get an input 
uInput = int((input("Enter The Number To Print Mutliplication Table of --  ")))
print(f"Multiplication Table of {uInput}")
#2) use a for loop to range 10 i.e 1,11
for i in range(1,11):
    #3) just put the user input and i value and mutliply them at each step -> and print each step.....
    print(f"{uInput} x  {i} = {uInput*i}")


#6)Prime Numbers: Write a program to find all prime numbers between 1 and 100 using a loop.


for a in range(2,100):
    is_Prime = True
    for c in range(2,a):
    	if a % c == 0:
         is_Prime = False
         break
    if is_Prime:print(f"{a} -- a prime no")
    elif is_Prime ==False:print(f"{a}  -- not a prime no")