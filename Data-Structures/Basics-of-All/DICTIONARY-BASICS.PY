# DICTIONARY - > {KEY:VALUE,} ----> ordred(form python 3.6+), mutable &
# keys-> must be immuatble data type

#i.e keys can be string , no's and tuples.....

#eg :-

my_dict = {1:"rizwan",2:"furqan",3:"ahmad","whoami":"furqan"}
print(my_dict) 

#op's 

print(my_dict[1]) #1)keys assicated value 
print(my_dict["whoami"])#-keys associated value  -> if string key - > in " "


my_dict['whoami2'] = "human-being" #2)adding new - Key:value from end....
print(my_dict)

del my_dict[1] #give here key of which pair to remove...

print(my_dict) #3)deletes the 1 key-pair

#4) check existence

if 2 in my_dict:
    print("Exist...")
else:
    print("No....")



# Dictioonary App's :- #impt....
# 1) used to store login credentials (whether hashed / not) 
# 2) mapping for quick lookups and Apis with json(used within array/list)
#3) stroing configs,logs with detailed metadata



								#Dictionary Basic Methods

newDictionary = {"username1":"xjfdkjjhei","username2":"djkfjdjf"}
#.keys() #gives all keys of given / specified dictionary
print(newDictionary.keys())

#.values() #gives all values of given / specified dictionary
print(newDictionary.values()) 

#.get() #gives value  of given / specified key & 
#if not found -> specified error show(optional)
print(newDictionary.get("username1","Not-Found")) #if not found -> returns the error we gave -> Not-Found....