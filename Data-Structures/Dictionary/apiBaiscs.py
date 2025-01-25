import requests

# Replace with the IP you want to query
ip_address = input("ENTER THE IP TO FIND - ")

# Sending the request for a specific IP
response = requests.get(f'https://ipinfo.io/{ip_address}/json')

if response.status_code == 200:
    ip_data = response.json()
    for key,value in ip_data.items():
        print(f"{key} - {value}")
        print("---------")
    print(ip_data)
else:
    print(f"Error: {response.status_code}")
