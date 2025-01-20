#3) Tuple ()     -> ordered , immuatble , allow duplicates
#eg_ a = (2,5,5,hi)
#op's

a = (1,2,3)
b = (4,5,6)
ab = a + b
print(ab) #1) conacation of tuples....

aDouble = a*2
print(aDouble) #2) repetion/multiplying Tuple

print(aDouble[0:3]) #3)slicing as it is ordred,,,,

#common use-> 1) storing value not  modified / constant   eg:
cordinates = (35.525,70.355) #cordinates for specific place usually not changes
dates = ('20-05-2024','21-05-2024') #specific dates which are impt can be stored in tuple..

# 2)return mutliple values from functions
def user_info():
    username = input("Enter Your Name")
    password = input("Enter Your Password")
    return (username,password) #return here two variables  in tuple 

print(user_info()) #but in tuple.....