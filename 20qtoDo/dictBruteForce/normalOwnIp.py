import requests
response = requests.get("https://api.ipify.org?format=json")
ip = response.json().get('ip')
print(f"SENDING REQUEST FROM IP - {ip}")