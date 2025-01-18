#qs 1) print only even indexed elements in the following list :-
tools = ["red","green","blue","yellow","Black"]
for idx,tool in enumerate(tools): #if we don't mention start then by def -> start 0
    if(idx % 2 == 0):
         print(idx,tool)
         
#qs 2) find the idx of the word "hacking" - if in list , otherwise -> not found
words = ["Python","Javascript","Security","Hacking","Linux"]
for idx,word in enumerate(words): #By def start 0 -> & we want that 
    found = False
    if(word == "Haacking"):
        print(f"index of {word} = {idx}")
        found = True
        break #The time we find exit as -> if not it will go to next 
if not found:
    print("NOT FOUND....")

#little brute-force
import time
usernames = ["admin"]
passwords = ["abcdef","smartshankar","instagarm212","hi","jdfjfdjdsl","eiorjhkskf","sdjkjhewriwo","wuireujhkdfhsfhiewurnfjk","eiowrjwejnrjkh"]
#enumerate use here-> 
for idx1,username in enumerate(usernames,start=1):
    for idx2,password in enumerate(passwords,start=1):
        time.sleep(0.2)
        print(f"Trying {username} for {password} [{idx2}/{len(passwords)}]")


