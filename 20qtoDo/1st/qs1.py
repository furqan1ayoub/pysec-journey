#make a program / tool using functions & loops -> where options include different tools i.e
#1) count vowels in words 2) reverse a string & check if it is a palindrome 3) check odd & even no's 4) count in a word frequency 5) guess-game

#1st step:- make the tools 
#1)count vowels 
def countVowelFunc():
    inputWord = input("Enter The Word - ")
    if inputWord.isnumeric():
        print("Please enter a valid word, not a number.")
    else:
        sum = 0
        vowels = "aeiouAEIOU"
        for eachChar in inputWord:
            if eachChar in vowels:
                sum+=1
                print(eachChar)
        print("Total Vowels -> ",sum)
#2) reverse a string & check if it is a palindrome
def revPalindFunc():
    inputWord = input("Enter The Word to check - ")
    print("The Word is -> ",inputWord)
    newRword = ""
    if inputWord.isnumeric():
        print("Enter Valid word, not a number")
    else:
        for eachWord in inputWord:
            newRword = eachWord + newRword
        print("The Reverse is -> ",newRword)
        if(inputWord == newRword):
            print(" ' ",inputWord," 'is a Palindrome")
        else:print(" ' ",inputWord," 'is not a palindrome")
#3) check even and odd no :-
def evenOddFunc():
    inputNo = input("Enter The No to check - ")
    try:
        inputNo = int(inputNo)
        if inputNo % 2 ==0 :print(inputNo ,"is an Even no")
        else:print(inputNo ,"is an Odd no")
    except ValueError:print("Enter A Valid no.")

#4)each-word frequency & total words
def wordFreqfunc():
    inputword = input("Enter The Sentence  to check - ")
    dictStore = {}
    storeList = inputword.split(" ")
    sum = 0
    for eachChar in storeList:
        sum+=1
        if eachChar in dictStore:
            dictStore[eachChar]+=1
        else:dictStore[eachChar] = 1
    for key,item in dictStore.items():
        print(f"{key} - {item}")
    print("Total words - " , sum)
#5) guess game withe 3 limits
import random
def guessGame():
    robot = ["red","green","yellow","orange","sky blue","parrot","brown","grey"]
    robotGuess = robot[random.randint(0,len(robot)-1)]
    limit = 0
    while limit<3:
        inputGuess = input("Enter the Color Robot has Guessed - ").lower()
        if not inputGuess.isnumeric():
            if robotGuess == inputGuess:
                print("CORRECT✔ GUESS~ CONGRATS\nTHANKS FOR PLAYING \n ")
                break
            elif robotGuess !=inputGuess and limit <3 :
                limit+=1
                print('INCORRECT GUESS \t Only left limit -> ' ,3-limit )
                print(f"RobotGuess - {robotGuess}\n Your-Guess {inputGuess}")
            else:
                print("SORRY -- YOU LOST THE TIME")
                print("GOOD LUCK NEXT TIME ✔")
                break
        else:
            print("ENTER alphabets not numbers ")

#call all and in one go 

import time
def fullProject():
    print("\nWELCOME TO THE PROJECT 🚀")
    print("-"*30)
    playOrNot = input("Want to play y/n  ").lower()
    while playOrNot =="y":
        print("Game is Starting....")
        time.sleep(0.9)
        print("CHOOSE A TOOL \n")
        a = "1️⃣ Count vowels \n2️⃣ Reverse & check palindrome \n3️⃣ Even or odd check \n4️⃣ Word frequency \n5️⃣ Guess game"
        print(a)
        chooseInput = input("Enter The Options to Play(q to exit) -  ")
        if chooseInput =="1":countVowelFunc()
        elif chooseInput=="2":revPalindFunc()
        elif chooseInput=="3":evenOddFunc()
        elif chooseInput=="4":wordFreqfunc()
        elif chooseInput=="5":guessGame()
        elif chooseInput=="q":
            print('THANKS FOR PLAYING ')
            break
        else:print("ENTER VALID OPTIONS")
    if playOrNot == "n":print('- 	THANKS FOR PLAYING   	-')
fullProject()


#✔ Without if __name__ == "__main__": → The script runs every time, even if imported.
#✔ With if __name__ == "__main__": → The script only runs when executed directly.

if __name__ == "__main__":
    fullProject()


"""
if __name__ == "__main__": ensures that the script runs only when executed directly and not when imported into another script.

Without it → fullProject() runs every time, even if imported.
With it → fullProject() runs only when you execute the script directly.
"""