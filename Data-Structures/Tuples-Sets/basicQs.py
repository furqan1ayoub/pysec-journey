#tuples => type of data structure used to store constant values as it is immutable & ordered..
#also used in fucntion to return more than 1 elemenet return (a + b)
# denoted by -> ()

#qs1)create a tuple and access its elements 
tupel1 = ("1","2","3","4")
#way1)
for idx,eachNo in enumerate(tupel1):
    print(idx,eachNo)
#way2
print(tupel1[0])

#qs2) create a single element tuple and check its type
singelTuple = (2,)
print(type(singelTuple))

#qs3) try to modify the tuple
#singelTuple[0]  = "not 2 but 3"  // error cause immutable so can't directly assign new values

#q4) find the length of tuple using len()
print(len(singelTuple)) # 1

#qs5) 5.	Unpack a tuple into variables 
tuple2  = ('user1', '192.168.1.1', 'success')
(username,ip,status_code) = tuple2
print(username)
print(status_code)

#using slcing on tuple -> get subrange
tuple5 = ("hi","my","name")
print(tuple5[1:3]) #output - ('my', 'name')

#								Sets

# used mostly to -> 1) remove duplicates from given data 2) or to see common elements / union every elements in list

list1 = [2,5,5]
print(set(list1)) #removed 5 
#lly
list2 = [5,3,5]
print(set(list1).intersection(set(list2)))

# or we can store too value like
set1 = set(list1)
print(set) #removed 5

set2 = set(list2)
print(set1.intersection(set2)) #5
print(set1.union(set2))
#can save this too & make both into one....
tupleBoth = set1 | set2
print(tupleBoth)