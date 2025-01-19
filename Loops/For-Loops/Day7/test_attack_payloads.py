import time #simulate kinda real....

#Use nested loops to go through each combination of payload and endpoint.
#For each combination, print a message simulating testing of that input on that part of the website.

#Example of Payloads (malicious inputs):
payloads = [
    "<script>alert('XSS')</script>", 
    "<img src='x' onerror='alert(1)'>", 
    "<svg/onload=alert('XSS')>"
]

endpoints = [
    "user/register",  # user registration form
    "user/login",     # user login form
    "product/search", # product search box
    "comment/submit", # comment submission form
    "feedback/submit" # feedback form
]
#Python script:

#You're testing different payloads (attack codes) on different endpoints (places in the web app where data is handled).


#Your Task:Use nested loops to go through each combination of payload and endpoint. 
# For each combination, print a message simulating testing of that input on that part of the website.

status_code = 400 #here for eg otherwise if the resposne is 200 then
for payload in payloads:
    is_correct_Payload = False
    for endpoint in endpoints:
        print(f"Testing Payload:-  {payload} - {endpoint} ")
        time.sleep(0.5)
        if status_code==200:
            print(f"Testing Payload:-  {payload} - {endpoint} ")
            is_correct_Payload = True
            break
    if is_correct_Payload:break