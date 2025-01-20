#2) SETS    { , }   -> 1) UNORDRED 2)only can HAVE IMMUTABLE ELEMENTS IN IT(like str,int,bool,,etc)  3) UNIQUE (NO DUPLICATES IN IT)
#eg my_set = {2,3,5,"apple",none}

my_set = {3,5,323,5,True} #unordred
print(my_set) #removes the duplicate 5

my_set.add("orange")
print(my_set) #unordred...

my_set2 = {23,3532,32,5} #unordred
#union 
print(my_set | my_set2) # combines 

#intersection -  
print(my_set & my_set2) # common element only -show i.e 5


#applications => remove itme dupplicacy from list (eg -> scanned ips)
#if more list convert them to sets then ->  compare sets to find the common and unique items
#or directly compare sets but unordred so array better for data org but dupplicay there

#eg - 
ips_list1 = ["x","y","z"]
ips_list2 = ["a","b","c","x"]
#find common ips
ips_set1 = set(ips_list1)
ips_set2 = set(ips_list2)
print(ips_set1 & ips_set2) #x is common....


#EMPTY SETS ->  set()

set2 = {} #EMPTY DICITIONARY
print(type(set2))#shows the dictionary 

#ALWAYS MAKE EMPTY SETS LIKE THIS....
set3 = set()#EMPTY SET...
print(type(set3)) #here it  shows set 
