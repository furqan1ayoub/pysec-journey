def add(input1,input2):
        return input1 + input2

def subtract(input1,input2):

        return input1 - input2

def multiply(input1,input2):
        return input1 * input2
def divide(input1,input2):
        try:
            return input1/input2
        except ZeroDivisionError:print("0 division error")

def calcBasic(input1,input2,inputOp):
    if input2.isdigit() and input2.isdigit():
        input1 = int(input1)
        input2 = int(input2)
        if inputOp=="+":
            result = add(input1,input2)
            print(result)
        elif inputOp == "-":
            result = subtract(input1,input2)
            print(result)
        elif inputOp == "*":
            result = multiply(input1,input2)
            print(result)
        elif inputOp == "/":
            result = divide(input1,input2)
            print(result)
        else:print("ENTER CORRECT OPERATION  ")
    else:print("ENTER VALID NUMBERS")
if __name__=="__main__":
    #for new reusable of new variables there in new import
    input1 = input("ENTER THE FIRST NUMBER - ")
    input2 = input("ENTER THE SECOND NUMBER - ")
    inputOp = input("ENTER OPERATION - ") 
    calcBasic(input1,input2,inputOp)