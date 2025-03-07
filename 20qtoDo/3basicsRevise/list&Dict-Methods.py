#list methods - 
#append 
list1 = []
list1.append(5)
print(list1)
#extend
list2 = []
list2.extend(list1)
print(list2)
#remove 
list2.remove(5) #first occurence of the element in the list
print(list2)
#pop
deletedelement=list1.pop(0) #0th index pe remove
print(list1,"Deleted element is ",deletedelement)
#count 
list5 = [3,5,3,9]
occurence=list5.count(3)
print("occurence of item 3 is - ",occurence)
#string to list then count the occurence
sentence = "this is my name is "
newArray = sentence.split(" ")
occurenceEachElement = newArray.count("is")
print(occurenceEachElement)

# 
ips = ["ip1","ip2","iptoFind192.168.21.8"]
if "iptoFind192.168.21.8" in ips:
    print("yes it is in the list at idx - ",ips.index("iptoFind192.168.21.8"))
else:print("not found--")


#dictionary - methods
dict1 = {"a":2,"b":5}
for key,value in dict1.items():
    print("key-",key)
    print("value - ",value)
    print("="*5)
#get
print(dict1.get("2","NOt found"))

#get values/insert
dict1["c"] = a={"a":3}
print(dict1["c"]["a"]) 
