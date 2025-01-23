#each word  occurence in string 
sentence  = "hi my name is furqan hi I am Good "
newSentence = sentence.split(" ")
dict_track = {}
print(newSentence)
for eachWord in newSentence:
    if eachWord in dict_track:
        dict_track[eachWord]+=1
    else:
        dict_track[eachWord]=1
print("Each Word in Sentence") 
print(dict_track)

#or shorcut
tracking_set = set()
for eachWord in newSentence:
    if eachWord not in tracking_set and eachWord !="":
        occurence = newSentence.count(eachWord)
        print(eachWord , " - ",occurence)
        tracking_set.add(eachWord)
        
#smallest and largest no in 2 lists
array1 = [2,5,6,9,234,2]
array2 = [2,589,25,2,5]

#m1) combine array 
combined_array = array1+array2
print("Largest No - ",max(combined_array),"- Smallest NO ",min(combined_array)) 


#m2) again combine array But long method
largest_no = combined_array[0] # for tracking from 1s element
smallest_no = combined_array[0] # same for tracking and comparing from 1st idx 
for eachNo in combined_array:
    if eachNo > largest_no:
        largest_no = eachNo
    elif eachNo < smallest_no:
        smallest_no = eachNo
print("Smallest NO - " , smallest_no)
print("Largest NO - ", largest_no )