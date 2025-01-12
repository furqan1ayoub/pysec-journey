import time #for realistic way show

# Define usernames and passwords
usernames = ["admin", "user", "guest", "john_doe", "jane_smith", "support", "root", "superuser", "manager", "employee"]
passwords = ["1234", "password", "admin", "secret123", "qwerty", "helpdesk", "toor", "strongpass", "secure123", "mypassword"]

# Simulate brute-force attack
for username in usernames:
    logged_in = False  # Flag to track successful login

    for password in passwords:
        print(f"Trying username: {username}, password: {password}")
        time.sleep(0.1)  # Simulate delay

        if username == "root" and password == "secure123":
            print("Successful Login!")
            print("------------------------")
            print(f"Username: {username}")
            print(f"Password: {password}")
            logged_in = True
            break  # Break out of the password loop
    if logged_in:
        break  # Break out of the username loop

print("Brute-force attack complete !")