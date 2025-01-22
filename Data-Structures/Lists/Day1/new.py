# Array Basic Questions -

# Basic -
#1)Create a list of numbers and print their sum

numbers = [2,5,6,5,0,2,5]
sum = 0 #box to put
for no in numbers:
    print(no)
    sum+=no
print("The Sum is - ", sum)

#2)Remove duplicates from a list of numbers

list1 = ["furqan","rizwan",5,5,"furqan"] #removing furqan and 5
list2 = []
#if want --ordred List--
for elem in list1:
    if elem in list2:    #checks if the element is list 2 if yes -> leave this Go to next 
        continue
    else:
        list2.append(elem) #append the one's not present in list2 -> i.e skips duplicates / already added ones.
print(list2)
#or 

#concise, efficient, and Pythonic way :- type conversion
new_tuple_ = set(list1)
print(new_tuple_)
"""Key Considerations:

If maintaining the original order is crucial, use Method 1.
For general duplicate removal and conciseness, Method 2 is preferred."""



#3) Write a pgm to count frequency of words in a given sentence   
sentence = "I love coding and I love learning"
checking_list = {}
new_sentence = sentence.split(" ") #splits by space => puts in array
print(new_sentence)
for eachWord in new_sentence:
    if eachWord in checking_list:
        checking_list[eachWord]+=1 #remember this is just adding if value/word present in the checking list  i.e if another word.. 1+1 =2 times
    else:
        checking_list[eachWord] = 1 #this is adding the value(each word) to key(1)
print(checking_list) #just check each ones' occurence /frequency

#do this...

#4) Write a program to find common elements b/w two Lists

first_list = ["1","2","3","4",5,"hello"]
second_list = [1,2,3,4,5,"hello"]
#two ways:-
#)long , ordred and indexed but -> long and hectic
for eachNo in first_list:
        if eachNo in second_list:
            print(eachNo,"- Common")
#)easy,precise,but unordred  -> set and then intersection.....

first_set = set(first_list)
second_set = set(second_list)
print(first_set.intersection(second_set))#finished.....

#or use => print(first_set & second_set)

#	Sort a list of numbers in descending order....

list66 = [2,5,5,839,93,5,34,5]
print(list66,"Before-> sorted")
#ascending -> 0,1,2
#descending-> 4,3,2,1
list66.sort(key=None,reverse=True)
print(list66,"After Sorted...")

#intermeditae...

""" 
•	Two sets largest and smallest number 
-> do agian :-   #3) Write a pgm to count frequency of words in a given sentence   
Focused Practice
•	IP Address Validation: Input Some Ip &  Check if IP exists in a list
•	Username Check: Input Some Usrename  username existence in a list
"""