#functions -> a way to make our code easy and well maintained
#once defined we call it simple instead again and again writing the same piece of shitty code

# practicals

def greet(name):
    print(f"your Name is {name} ")
greet("furqan")
print("take it as ........long code ....")
greet("rizwan") #again used instad of writing this again/ this is just eg-> we have long codes to run So for that


#return keyword -> returns a value -> which we can store and print & code after it never runs So we shouldn't write after it cause it will never runn...

def add(a,b):
    return a+b
#add(a,b) => only saves no print nothing
print(add(3,5))
#save for future and print too #for debugging used
value = add(35,2354)
print(value) #more modular as it saves value and prints too


#pass / .... ( elipsis)
def someFunc():
    ...
def someFunc2():
    pass
#both did same let us not cause error and do work on other code and come back when needed we just remove it 
#pass more used than ...

#arguments and parameters -> parameters are kinda variables in which value is given and used in function & arguments is where we put the values

#1) default keywords -> value provided in Parameters

def printName(name="furqan"):
    print(name)
printName()

#2) regular keywords -> value provided in Arguments

def printName2(name):
    print(name)
print("furqannnnnn")
#3) no args & keywords isn't type as not any having like greeting 

#4) variable position arguments (*args) -> a parameter  gets numbers of arguments and gets stored in a form of tuple
#eg 
def findAvg(*args): #args is just used we can put any name
    sum = 0
    length = len(args)
    for eachNo in args: #as args is now a kinda tuple so we can iterate over it
        sum+=eachNo
    return sum/length
avg=findAvg(1,2,52837,2,5,23,5) #put mutliple values here & are stored in args -> as tuple
print(avg)

#5) keywords positonal args (**kwargs) => stores in parameter as dictionary So parameter is now Dictionary
#and dictionary methods can be used too
#eg 
def details(**kwargs): #same -> can put any name def we put kwargs here
    for key,value in kwargs.items():
        print(f"{key} :-  {value}") #each key:value then to next -> in kwargs dict
        
        #we can't use return here like cause return after no code runs///so even 1st iteraion pe hi -> exit...
    print("or.")
    #or index one 
    for keys in kwargs: #keys only
        print(keys,"-----",kwargs[keys]) #as kwargs -> dict and kwargs[keys] -> will give value with respective Key 
        
        #same no return cause -> won't iterate & exits at first loop

print(details(name="Furqan", RollNo = 33, Address = "FAthe kadal..")) #these key:value gets stored in kwargs & kwargs is dicitonary & then dict methd






def functionName():
    print("hello")
    pass #without it runs / our choice to use it or not -> i will use
def function2():
    print("yo")
function2() #here it runs