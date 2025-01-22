#find common ips b/w two lists 
ips_list1 = [
    "192.168.0.1",
    "192.168.1.1",
    "10.0.0.1",
    "172.16.0.1",
    "8.8.8.8"
]

ips_list2 = [
    "192.168.0.1",
    "10.0.0.2",
    "172.16.0.1",
    "8.8.4.4",
    "1.1.1.1"
]
#2 ways 
#1) short concise 
set1 = set(ips_list1)
set2 = set(ips_list2)
print(set1.intersection(set2)) # or set1 & set2

#2)long than above but Ordered and more Controlled
for eachIp in ips_list1:
    if eachIp in ips_list2:
        print("Common IPS- ",eachIp) #customize 
        
	#which one to choose
 
"""
Both methods serve their purpose, and which one to choose depends on your specific requirements:

Use Approach 1 if performance and brevity are your priorities.
Use Approach 2 if you want an ordered and easily customizable process. """
#Recommendation:
"""
Use Approach 1 for efficiency and Approach 2 when you need finer control or deeper practice.

For a cybersecurity mindset:

Think about which approach is better for analyzing logs, scanning networks, or automating workflows where performance can be critical. Use sets for most cases!
"""

#q2) •	IP Address Validation: Check if IP exists in a list & give its index 
#q3) •	Username Check: Check username existence in a list

usernames_list1 = [
    "cyber_hawk",
    "tech_wizard",
    "shadow_byte",
    "dark_knight",
    "net_ninja"
]

usernames_list2 = [
    "shadow_byte",
    "fire_fury",
    "code_master",
    "net_ninja",
    "data_hunter"
]

# IP Address Validation (Q2)
input1ip = input("ENTER THE IP TO CHECK = ")
if input1ip in ips_list1:
    print(f"FOUND - {input1ip} in ips_list1 at index {ips_list1.index(input1ip)}")
elif input1ip in ips_list2:
    print(f"FOUND - {input1ip} in ips_list2 at index {ips_list2.index(input1ip)}")
else:
    print("NOT FOUND...!")

# Username Check (Q3) 
input2Name = input('ENTER THE NAME TO FIND - ')
if input2Name in usernames_list1:
    print(f"FOUND - {input2Name} in usernames_list1 at index - {usernames_list1.index(input2Name)}")
elif input2Name in usernames_list2:
    print(f"FOUND - {input2Name} in usernames_list2 at index - {usernames_list2.index(input2Name)}")
else:
    print("NOT FOUND..")

