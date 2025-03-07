#2 functions 1)do the array into the str and 2) put str values in the array sep by space

def intoArray(value):
    newValue = value.split(" ")
    return newValue
def intoStr(value):
    newValue = ','.join(value)
    return newValue

def arrayStrConvFunc():
    opt = input("ENTER THE OPTION \n 1- String to Array \n 2- Array to String \n - " )
    if opt == "1":
        try:
            value = input("ENTER THE STRING - ")
            array1=intoArray(value)
            print("The Array is \n",array1)
        except ValueError:
            print('ENTER CORRECT STRING')
    elif opt == "2":
        array = []
        try:
            while True:
                input1 = input('ENTER THE VALUE - ').lower()
                if input1 !="q":
                    array.append(input1)
                else:
                    print('YOUR ARRAY IS - ',array,"\n Converted to string ----")
                    string1 = intoStr(array)
                    print('STRING ->',string1) 
                    break
                  
        except ValueError:
            print('ENTER CORRECT Array')

if __name__ == "__main__":
    arrayStrConvFunc()