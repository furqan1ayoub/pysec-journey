"""while True:
    # some condition
    if some_condition:
        break"""

# a) sum Of no's until zero:-

a = int(input("Enter the no - "))
sum = 0
while True:
    if a != 0:
        sum += a
        a = int(input("Enter Next No. to Add "))
        print("PRESS 0 to Exit ")
    elif a == 0:
        print("The Sum of Numbers - ", sum)
        break
# b) factorial using loop i.e 5 ! = 5*4*3*2*1
inputNo = int(input("Enter the no to find - "))
i = 1
factorial_box = 1  # 1 because 0 multiplied by anything is 0
while i <= inputNo:
    factorial_box *= i
    i += 1
print(f"The factorial of {inputNo} is - {factorial_box}")


noInput = int(input("Enter The No first- "))
storePvalue = 0
while True:
    if noInput != 0:
        storePvalue = noInput
        noInput = int(input("Enter The No To Compare with Previous Value "))
        if noInput > storePvalue:
            print(f"{noInput} is Greater than {storePvalue}")
        elif noInput < storePvalue:
            print(f"{noInput} is Smaller than {storePvalue}")
        else:
            print(f"{noInput} is Equal to {storePvalue}")
    else:
        print("Exited...")
        break