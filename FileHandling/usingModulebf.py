#write into a file like 
with open("random.txt","w") as fileRandom , open("10k-most-common.txt","r") as userFile:
    pwdList = userFile.read().splitlines()
    print(pwdList)
    idx = 0
    for  eachUser in pwdList:
        fileRandom.write(f"user{ idx } {eachUser} \n")
        idx+=1
        