# Arrange each username with all passwords

def getUsernamePwd(usernameF, pwdF, inpFileName):
    try:
        with open(usernameF, "r") as fileUsername, open(pwdF, "r") as filePassword:
            for eachUserName in fileUsername:
                userN = eachUserName.strip()
                filePassword.seek(0)  # Reset pointer to start of password file
                
                for eachPassword in filePassword:
                    passW = eachPassword.strip()
                    saveUserPwd(userN, passW, inpFileName)
                
                addSeparator(inpFileName)

    except FileNotFoundError as e:
        print(f"❌ Error: File Not Found - {e}")

def saveUserPwd(userN, passW, inpFileName):
    try:
        with open(inpFileName, "a") as file2:
            file2.write(f"{userN} - {passW}\n")
    except ValueError:
        print("❌ Error: Something went wrong with the file name. Please try again.")

def addSeparator(inpFileName):
    with open(inpFileName, "a") as file2:
        file2.write("-" * 50 + "\n")

if __name__ == "__main__":
    userNamefile = "usernameFile.txt"
    passwordfile = "passwordFile.txt"
    inpFileName = input("Enter file name to save output: ") + ".txt"
    
    getUsernamePwd(userNamefile, passwordfile, inpFileName)
