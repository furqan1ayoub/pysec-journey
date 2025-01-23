#previosu Qs
#frequency of words in given sentences
sentence = "hi I love coding I love myself"
#change it to the array
newArray = sentence.split(' ')

#print(newArray)
tracking_dict= {} #for tracking the occurence Empty dictionary

for eachChar in newArray:
    if eachChar in tracking_dict:
        tracking_dict[eachChar]+=1 #adds the value 1 +1 lly if 2 set 2+1 (for tracking duplicate ones)
    else:
        tracking_dict[eachChar] = 1  # adds each character in Array as key -> in tracking_dict_dict & 1 if only onces as Value 

#see every words occurence....
print(tracking_dict) 

# sort array
sortedAscendingO = [1,2,3,4,5,6,7,8,9]
sortedAscendingO.sort(key=None,reverse=True)
#if we put like sortedDescO = sort(key=None,reverse=true) => None
print(sortedAscendingO)
#but copy in new array
sortedDescO = sortedAscendingO.copy()
print(sortedDescO)



#Qs :- 

array1 = [2, 5, 6, 9, 23, 35, 1]
#initilize / start for checking 
large_No = array1[0]

for eachNO in array1:
    if eachNO > large_No:
        large_No = eachNO
        #1st => 2 > 2 no next 5>2 yes 
        #large value value changed to 5 
        #next 6 > 5 yes now large no changed -> 6
        #... go an like at last largeNo = 35
        #but 1 > 35 False So large NO = 35
print(large_No)

#smallest & larges  no b/w two
array2 = [2,5,6,2]
array3 = [5,23,5,1,55]
combined_array = array2 + array3
#m1) combine array 
combined_array = array1+array2
print("Largest No - ",max(combined_array),"- Smallest NO ",min(combined_array)) 

#m2) again combine array But long method
largest_no = combined_array[0] # for tracking from 1st  idx element (initializing )
smallest_no = combined_array[0] # same for tracking and comparing from 1st idx 
for eachNo in combined_array:
    if eachNo > largest_no:
        largest_no = eachNo
    elif eachNo < smallest_no:
        smallest_no = eachNo
print("Smallest NO - " , smallest_no)
print("Largest NO - ", largest_no )


# Shorcut / Function  :- but not best for problem solving and building logic and often limited
#here as we combined 2 array in one so can make this....


print(max(combined_array)) #max no in array to find largest no in array
print(min(combined_array)) #min method  to find lowest no in array


