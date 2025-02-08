#                           Calculator

#s1) make the operations functions first 

#add
def addF(no1,no2):
    return no1 + no2

#sub
def subF(no1,no2):
    return no1 - no2

#multiply
def multF(no1,no2):
    return no1*no2

#division

def divF(no1,no2):
    if(no2 == 0):
        return "Zero Division Error"
    return no1/no2

#s2) prompt to users

#function

def Calculator():
    print("----Calculator---- \n !! Welcome !!")

    print("Read Rules")

    print("Enter 1 to add ""+"" ")
    print("Enter 2 to Subtract ""-"" ")
    print("Enter 3 to Multiply ""*"" ")
    print("Enter 4 to Divide ""/"" ")

    print("OR")
    print("PRESS q to leave")

    #ask for input

    while True:
        operations = input("Enter the Operation - ")

        if operations.lower() =="q":
            print("Thanks for Playing. \n Exited.")
            break
        else:
            if operations not in ["1","2","3","4"]:
                print("invalid option choosed ")
                continue #continue to next 
            try:
                input1= float(input("Enter first no - "))
                input2 = float(input("Enter second no - "))
            except ValueError:
                print("Invalid input ")
                continue #enter again/ do again this loop
            if operations == "1":
                    op = "+"
                    value = addF(input1,input2)
                    print(f"{input1} {op} {input2} = {value}")
            elif operations == "2":
                    op = "-"
                    value = subF(input1,input2)
                    print(f"{input1} {op} {input2} = {value}")
            elif operations == "3":
                    op = "*"
                    value =  multF(input1,input2)
                    print(f"{input1} {op} {input2} = {value}")
            elif operations == "4":
                    op = "/"
                    value = divF(input1,input2)
                    print(f"{input1} {op} {input2} = {value}")
Calculator()