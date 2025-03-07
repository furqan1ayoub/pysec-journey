#file handling -1) working with the files to store the data permanently or 2)to log the programs activities/problem faced ,&
#3) to use file data i.e large into the pgm
#2 ways to deal with the files
"""#1) open() alone
file = open("random.txt","a")
file.write("\nappendded this one")
file.close()"""
#2) with -> more used and recommended as it closes the file automatically and is less iin syntax
import time
def bruteforce(filePwd,fileUsername):
    with open(filePwd, "r") as pwdfile,open(fileUsername,"r") as userfile:
        pwdlist = pwdfile.read().splitlines()
        userlist = userfile.read().splitlines()
        print("---- STARTING BRUTE FORCE -----")
        for eachUser in userlist:
            loggedIn = False
            for eachPwd in pwdlist:
                time.sleep(0.5)
                print("trying for usr - ", eachUser)
                print(f"TRYING - {eachUser} - {eachPwd}")
                if eachUser == "root" and eachPwd == "pussy":
                    print(f'--- SUCCESS FOUND! --- \n correct -> {eachUser} - {eachPwd}')
                    loggedIn = True
                    break
                else:print('--- FAILED ---')
            if loggedIn:break
            
if __name__ == "__main__":
    bruteforce("10k-most-common.txt","top-usernames-shortlist.txt")