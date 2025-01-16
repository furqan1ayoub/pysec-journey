import time
#Brute Force Simulation: Write a program that simulates a brute force attack by trying all possible combinations of a 4-digit PIN.
# Display each attempt, and stop when the correct PIN (e.g., 1234) is found.
#zfill:-


# Added PINs for each user
users = [
    {"name": "Alice Johnson", "address": "123 Maple Street", "pin": "4821"},
    {"name": "Bob Smith", "address": "456 Oak Avenue", "pin": "7390"},
    {"name": "Charlie Brown", "address": "789 Pine Road", "pin": "1234"},
    {"name": "Diana King", "address": "321 Birch Lane", "pin": "5678"},
    {"name": "Ethan Hunt", "address": "654 Cedar Blvd", "pin": "9012"},
    {"name": "Furqan Ayoub", "address": "987 Walnut Street", "pin": "2468"},
]

import time
def attackfunc(user):
    print("Starting..........")
    print("--------------------------")
    print("Searching For Details...")
    print("Getting Details.....")
    time.sleep(1)
    print("found....")
    print(f"Name :- {user['name']}")
    print(f"Address :- {user['address']}")
    print("---------------------------")
    time.sleep(1)
    print("Trying Brute Force......")
    print("-----------------------------")
    for attempt in range(0,1000):
        attempt = str(attempt).zfill(4)
        print(f"Trying PIN: {attempt}")
        time.sleep(0.1)
        if(attempt == user['pin']):
            print(f"PIN FOUND for NAME - {user['name']} ADDRESS - {user['address']} PIN - {attempt}")
            break
def eachUser():
    for user in users:
        attackfunc(user)


eachUser()
				
    
    
    
    	#rjust....
"""inputPassword = input("Enter Your Password: ")
length_pwd = len(inputPassword)
print(inputPassword[-2:])
# Mask all but the last two characters with 'x'
if length_pwd > 2:
    hidden_Password = inputPassword[-2:].rjust(length_pwd, "x")
else:
    hidden_Password = inputPassword  # Show as is if the password is too short

print("Your password with the last 2 digits visible:", hidden_Password)

"""