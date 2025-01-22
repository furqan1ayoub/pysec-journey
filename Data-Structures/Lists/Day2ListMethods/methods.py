#                                                        """Methods of Lists in Python"""

#1) append -> adds items to end of list
array1 = []
input1 = input("What is Your Name - ")
array1.append(input1)
print(array1)

#2) extends -> combine another list to one list
array2 =["hello"]
array2.extend(array1)
print(array2)

#3) remove -> remove first occurence of Given ELEMENT
array3 = ["hello","hello","hi",32]
array3.remove("hello") # first hello->removed
print(array3)


#4) pop -> removes and returns idx element -> from a specified list

#save that one
last_element = array3.pop(0)     #default(if not writtne some idx) -> last

print(array3)
print(last_element,"This is removed")


#5) index -> return the idx of the first occurence of the given value
a = [2,5,"hello"]
print(a.index("hello"))
#outpue -> 2
#usefull in seeing the occurence of some impt things

#6) reverse -> returns the list in reverse form
grettings = ["hi","how are you","bro","!",3] #just reverse 
grettings.reverse()
print(grettings)

#7) sort ->  sort basically -> sorts same data types -> in ascending(reverse = false/don't write anything in bracket)
# / descending(this is 'reverse = true' here , not as above one )
a= [2,5,342,523,1]
#a = ["hi",2,"hello",342] =====> \Error/
a.sort(reverse=False) #key:None,reverse = true -> descending order
print(a)




#8) count() => counts-> occurence of the element  and return no (we can save this)
logs = ["INFO", "ERROR", "INFO", "ERROR", "INFO"]
print(logs.count("ERROR"))  # Output: 2



#9) insert() => insert an element to the given idx
array23432 = ["hello",2]

array23432.insert(1,"Sir")

print(array23432) # outpupt => ["hello","Sir",2]



#10) clear() => clears the current list 

temp_data = ["username", "password"]
temp_data.clear()
print(temp_data)  # Output: []


