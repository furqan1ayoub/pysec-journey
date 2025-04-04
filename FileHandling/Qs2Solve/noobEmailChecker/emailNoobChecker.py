#only basic validation

def emailValidator(eachEmail):
        with open('validEmail.txt','a') as fileEmails:
            if "@" in eachEmail and "." in eachEmail.split("@")[1] and not any(eachChar in eachEmail for eachChar in "'\/!#$%^&*()-+=[]{ }|~`")  :
                fileEmails.write(f"{eachEmail}\n") 
            else:print(eachEmail,"-- not a valid")    

def countValidEmails():
    inputFile = input("Enter the filename to see(no ext) - ") + ".txt"
    with open(inputFile,"r") as validEmails:
        count = 0
        for eachline in validEmails:
            count+=1
        print("Valid Emails = ", count)
def emailChecker(filename):
    with open(filename,"r") as randEmailfile:
        total=0
        for eachLine in randEmailfile:
            #get each email
            eachEmail = eachLine.strip().split()[1]

            total+=1
        
            emailValidator(eachEmail)
        print("Total Random emails - ",total)
    countValidEmails()
emailChecker("randomEmails.txt")