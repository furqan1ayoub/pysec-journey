#validate emails in random emails
#
def validateEmails(eachEmail):
    try:
        if "@" in eachEmail and "." in eachEmail.split("@")[1] and not "." in eachEmail.split("@")[0] and not any(eachChar in eachEmail for eachChar in "'\/!#$%^&*()-+=[]{ }|~`"):
            with open("valid-emails.txt","a") as ValidEmailsfile:
                ValidEmailsfile.write(f"{eachEmail}\n")
                
        else:
            with open("invalid-emails.txt","a") as inVAlidEmails:
                inVAlidEmails.write(f"{eachEmail}\n")
    except FileNotFoundError:print("FILE NOT FOUND")
            


def parseEmails(filename):
    try:
        with open(filename,"r") as rEmailFile:
            total_random_emails =0
            for eachLine in rEmailFile:
                eachEmail = eachLine.strip().split()[1]
                print(eachEmail)
                total_random_emails+=1
                print(total_random_emails,"- total emails")
                validateEmails(eachEmail)
    except FileNotFoundError:print('- FILE NOT FOUND -')
parseEmails("randomEmails.txt")