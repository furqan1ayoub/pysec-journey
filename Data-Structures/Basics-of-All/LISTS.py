# 								Data Structures

#string,int,boolean,None -> i studied 

#1) List    []   ->     1) ordred 2) mutable 3) duplicate allowed...
#op's - 

my_list = ["1",2,True,4,2]
print(my_list[0]) #1) accessing list elemnents

my_list[0] = 1 #2) modifying element
print(my_list) 

my_list.append(3) 
print(my_list) #3)appended / added element from last

my_list.remove(2) 
print(my_list) #4)remove first occurance of 2 if multiple times / duplicate


print(my_list[0:2])  #5)slicing

#6)sorting
my_list.sort(key=None,reverse=False)
print(my_list)

my_list.sort(reverse=True)
print(my_list)#reverseSroting


#applications of sets- storing ips and data in ordred way
# and also if we have some duplicates
# We can remove it by changing the array to the set i.e type conversion
# -> which remove the duplicacy but are unordred and don't contain immutable elements

ip_lists = ['192.168.0.1',"192.168.0.2","192.168.0.1"]
unique_ips = set(ip_lists) #type conversion / Explicity conversion

print(unique_ips) #REMOVES ALL DUPLICATE ONES 