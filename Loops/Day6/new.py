#1) Reverse a string using loop 


oStr = "hello"
revStr = "" #make an empty string to make it more organized and to store in it....
for i in oStr:
    print(f"Adding {i}....")
    #here just keep on adding the i iterators value in the -> empty made revStr (like -> box )
    revStr = i + revStr #also revStr value will be then reverse of oStr 
print(f"The Reverse of {oStr} => {revStr}")


#2)   Check if a stirng is a palindrome
#Palindrome -> the reverse of string is same as original 

#here we also need to check the validation of input so did if else inner -> for
userInput = input("Enter the String to Check - ")
print("Your Input -",userInput)
checkingStr = ""

if userInput.isdigit(): #this will tell us the input is valid to check or integer to not check in for
    print("Not a Valid input ",userInput)
else:
    userInput = userInput.lower()
    for char in userInput:
        checkingStr = char + checkingStr
    if checkingStr == userInput:
        print(f"{checkingStr} is a palindrome...")
    else:
        print(f"{checkingStr} is not a palindrome x")
        
        
#3) Check NOw in  list and Get from it the palindrome and insert in another list

words = ["level", "radar", "python", "madam", "hello", "racecar", "world", "civic", "example", "deified"]
palindromeOnly=[] #to store palindromes...

for word in words: #gives one word full like -level
    print("word")
    word = word.lower()
    #impt :- local scope 
    checkStr="" # add here as due to make the string empty to check for others too..........
    
    for char in word: #checks now each word like - l then -  e then v ......
        checkStr = char + checkStr #add reversly in checkstr
    if(checkStr == word):
        print(f"{checkStr} , is a Palindrome..........")
        palindromeOnly.append(checkStr)
    else:
        print(f"{checkStr} is not  a  palindrome.......x")
print("End....\n")
print("palindrome only - ",palindromeOnly)