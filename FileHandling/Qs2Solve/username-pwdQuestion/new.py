#pair all passwords with each usernames given in the file
#function 1)
def parseFile(usernameFile,passwordFile,):
    try:
        with open(usernameFile,"r") as uNameFile , open(passwordFile,"r") as pwdFile: # , we can add two files 
            for eachUsername in uNameFile:
                eachUsername = eachUsername.strip()
                print("------------------")
                #now password iteration
                pwdFile.seek(0) #resets file pointer to 0 
                #this one is for resetting after it reaches to end / pointing to beginning for next iteration
                for eachPwd in pwdFile:
                    eachPwd = eachPwd.strip()
                    print(f"{eachUsername} - {eachPwd}")
                    save_to_File(eachUsername,eachPwd)
                #now for in b/w users sepeartor as --------
                try:addSeparator("username-pwdList.txt") # here cause next iteration yaaha ke baad hogi
                except FileNotFoundError:print("FILE NOT FOUND ")
    except FileNotFoundError:print("No File Found")

# save to file 
def save_to_File(eachUsername,eachPwd):
    with open("username-pwdList.txt","a") as usernamePwdFile:
        usernamePwdFile.write(f"{eachUsername} - {eachPwd} \n")
# for in b/w seperator for 
def addSeparator(inpFileName):
    with open(inpFileName, "a") as file2:
        file2.write("-" * 50 + "\n")

parseFile("usernameFile.txt","passwordFile.txt")           