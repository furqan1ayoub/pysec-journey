#store and access username & pwds in dictionary
Userdetails={"user":"pwd1","u2":"pwd2"}
for username,pwd in Userdetails.items():
    print(f'Username - {username} , Password - {pwd}')
    
#check username's existence or not
uNameToCheck = Userdetails.get("user","N")
if uNameToCheck:
    print("Found")
else:print("Not Found")
#or simpley only if we have to check its value if it is there
print(Userdetails.get("uE","NOT FOUND..."))

#count word frequency in a string
sentence = "this is a random sentence this is not a meaningfull sentence"
array1 = sentence.split(" ")
dict_t = {}
for eachValue in array1:
    if eachValue in dict_t:
        dict_t[eachValue]+=1
    else:
        dict_t[eachValue] = 1
print(dict_t)


#update pwd for given username
#Userdetails={"user":"pwd1","u2":"pwd2"}
Userdetails["u2"] = "IAMFIMDMDMDM"
print(Userdetails)

# ip Mapping -> to Dictionary
#- > ip mapping to dictionary
devices = [
    "Router", "Switch", "Firewall", "Server", 
    "Access Point", "Laptop", "Desktop", 
    "IP Camera", "NAS", "Load Balancer"
]
ip_addresses = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3", 
    "192.168.1.4", "192.168.1.5", "192.168.1.6", 
    "192.168.1.7", "192.168.1.8", "192.168.1.9", 
    "192.168.1.10"
]
dict = {}
for idx,value in enumerate(devices): #we just used idx in here cause to pair -> device with respective idx value in ip_addresses
    dict[value] = ip_addresses[idx]
print(dict)
#now getting all key:value in sequenced way(just for practise)
for devices,ips in dict.items():
    print(f"Device:- {devices} & IP :- {ips}")
    

#6) 2d list to dicitionary -> to dictionary (in form of )-> {device :ip}

device_list = [
    ["Server_A", "192.168.1.100"],
    ["Database_Server", "192.168.1.101"],
    ["Web_Server_01", "192.168.1.102"],
    ["Firewall", "192.168.1.1"],
    ["Router", "192.168.1.1"],
    ["Switch_01", "192.168.1.254"],
    ["IoT_Device_1", "192.168.1.200"],
    ["Workstation_01", "192.168.1.50"],
    ["Printer_A", "192.168.1.150"],
    ["Security_Camera_01", "192.168.1.220"]
]
dv_ip = {}
for eachArray in device_list: # eachArray is now where we use indexing to put into dictionary
    dv_ip[eachArray[0]] = eachArray[1] #0-> device 1-> ip
print(dv_ip)
for dv,ip in dv_ip.items():
    print(f"DEVICE - {dv}    & \t IP - {ip}")
    print(" ")


#api & access elements in it

import requests

lat = input("ENTER LATITUDE:-  ")
long = input('ENTER LONGITUDE :- ')
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("Error.....")

for eachkey,values in data.items():
    print(f"- {eachkey}  - {values}")
temp = data["current"]["temperature_2m"]
print(f"THE TEMPERATURE IS :  {temp}")


#new request 

city_name = input("ENTER THE CITY NAME ")
new_url = f"https://goweather.herokuapp.com/weather/{city_name}"

response = requests.get(new_url)
if response.status_code==200:
    data = response.json()
    print(data)
    print(data["forecast"][1].get("day"))
else:
    print("NOT FOUND...")


#random stuff
devices = [
    "Router", "Switch", "Firewall", "Server", 
    "Access Point", "Laptop", "Desktop", 
    "IP Camera", "NAS", "Load Balancer"
]
ip_addresses = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3", 
    "192.168.1.4", "192.168.1.5", "192.168.1.6", 
    "192.168.1.7", "192.168.1.8", "192.168.1.9", 
    "192.168.1.10"
]

for idx,value in enumerate(devices):
    print(f"device -> {value} , ip -> {ip_addresses[idx]}")