#Questions Basic

#Store & Access Usernames & Passwords
userDetails= {
	"furqan1":"isdwamfurqd121",
	"Ahmad":"abcdPwd121",
	"xxrumourxx":"hacker234",
	"snatcher":"1233245"
}
#accessing each one by one
print(userDetails["snatcher"]) #one-by-one
#all-in-one
for username,pwds in userDetails.items(): #each iteration key:value 
    print(f"USERNAME - {username} PASSWORD - {pwds}")

#2)check any Password there or not
inputUsername = input("ENTER THE USERNAME TO CHECK - ")
usernameToCheck = userDetails.get(inputUsername)
if usernameToCheck :print("Found...")
else:print("NOT FOUND ")

#3) Count Word Frequency in a string
string1 = "Hello My Name is My Furqan Furqan"
newArray = string1.split(" ")
#empty dict
tracker_dict = {}
for eachWord in newArray:
    if eachWord in tracker_dict:
        tracker_dict[eachWord]+=1
    else:
        tracker_dict[eachWord] = 1
print(tracker_dict)

#4) update password for give Username => furqan pwd -> whoamiFurqan121
userDetails["furqan"] = "userDetails"
print(userDetails) #done 




#5)  - > ip mapping to dictionary
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
devices_ip = {}

for i in range(len(devices)):
    devices_ip[devices[i]] = ip_addresses[i]


for dev,ip in devices_ip.items():
    print(f"DEVICES ' {dev} ' IP - {ip}")


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

device_info={}

for alllist in device_list:
    device_info[alllist[0]] = alllist[1]
print("---------")
print(device_info)
#collect pairs....
for device2,ip2 in device_info.items():
    print(f"DEVICE---- {device2}      , IP   ----- {ip2}")