#basics #real-eg
import requests
response = requests.get("https://meowfacts.herokuapp.com/")
data = response.json()
for eachKey,value in data.items():
    print("KEY - ",eachKey)
    print("DATA - ",value)
#login

url = "http://testphp.vulnweb.com/userinfo.php"

usernames = ["hanief","furqan","abcd","nobody","instagarm","test"]
passwords = ["abcd","efghi","idkwhatis",2234,"tdkfjds","test"]
while True:
    details = {}
    logged_in = False
    for idx,eachUsername in enumerate(usernames):
        details["uname"]=eachUsername
        details["pass"]=passwords[idx]
        response = requests.post(url,data=details)
        data = response.content.decode("utf-8")
        print(response.status_code)
        try:
            if "Credit card number:" in data:
                print("logged-in")
                logged_in = True
                break
            else:
                print("invalild username and pwd")
        except ValueError:
            print("Response is not in JSON format")
    if(logged_in):
        print("SUCCESS ! LOGGED IN")
        print("USERANME - ",details["uname"])
        print("USERANME - ",details["pass"])
        break
    