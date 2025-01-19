#1)find all prime no's  from user's input
userInput = int(input("Enter the Number - "))
for i in range(2,userInput+1):
    is_Prime = True
    for j in range(2,i):
        if (i % j == 0):
            is_Prime = False
            break
    if is_Prime:print(f"{i} is  a prime no. ")
    elif not is_Prime:print(f"{i} is not a prime no. ")
            
            
#2) print pattern

for i in range(7,1,-1):  #visit copy if not getting
    for j in range(1,i): 
        print("*",end="") 
    print()

#3) palindrome & put it in list
words = ["racecar", "hi", "madam", "noon", "clone", "yo", "cat", "run", "smile", "mf"]
onlyPalindromes= []
for word in words:
    checker_str = "" #local scope
    for char in word:
        checker_str =  char + checker_str
    if(checker_str == word):
        onlyPalindromes.append(checker_str)
    else:
        print(f"{word}=> not a Palindrome")
print("Only Palindromes -> ", onlyPalindromes)

#4) normal brute force with ---Enumerate function (built-in)

username = ["shakeel","casteCollege"]
passwords = ["P@$$w0rd123", "Secure_Pass","VishnuSir", "MySecretCode", "StrongPassword42","Hello@123"]
import time
for idx1,eachName in enumerate(username):
    passWord_found = False #scoping
    for idx2,eachPassword in enumerate(passwords,start=1):
        print(f"TRYING {eachName} - {eachPassword}  [{idx2}/{len(passwords)}]")
        time.sleep(0.6)
        if(eachName == "casteCollege")and(eachPassword == "VishnuSir"):
            print(f"LOGGED IN ! ")
            print(f"--------<  {eachName} - {eachPassword} [{idx2}/{len(passwords)}] -------<")
            passWord_found = True
            break #break out of password array loop
    if passWord_found:break #break out of username loop 


# while

#1) FIND larges no from the list user inputs...
user_playing = input("ENTER YOU NAME - ")
userInputNo = int(input("\nENTER THE NUMBER - "))
storingNo = None
while True :
    if(userInputNo != 0):
        storingNo = userInput
        userInputNo = int(input("ENTER THE NUMBER TO COMPARE  - ")) #each time checked...
        if userInputNo == 0:  # If the user enters 0, stop the loop
            print("Thanks for playing....")
            break
        if(userInput > storingNo ):print(f"{userInput} is Greater than {storingNo}")
        elif(userInput < storingNo ):print(f"{userInput} is Less  than {storingNo}")
        else:print(f"{userInput} is Equal than {storingNo}")
    else:
        print(f"THANKS FOR PLAYING.... {user_playing}")
        break
    
#unitl username isn't admin and password not "hello " => Prompt User to 
#& Add attempt too Only after 5 attempts -> then block

attempts = 0
username1 = input("ENTER YOU NAME - ")
password1 = input("ENTER YOU PASSWORD - ")
while True:
    if (username1 != "admin" or password1 != "hello" ):
        attempts+=1
        if(attempts <= 5):
            username1 = input(f"ENTER Again {6 - attempts } Attempts  left...  \n YOUR NAME - ") #above again at each loop checked
            password1 = input(f"ENTER Password Again   \nYOU PASSWORD - ") #same again at each checked
        else:
            print("TOO MANY ATTEMPS TRY AGAIN LATER.....")
            break
    else:
        print(f"--------<  SUCCESS ! CORRECT CREDENTIALS THANKS FOR PLAYING -------<")
        break