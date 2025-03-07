#lambda functions
square = lambda x:x*x
print(square(3))
add = lambda a,b:a+b
print(add(3,9))
#map
list1 = [1,2,3,4,5]
list2 = list(map(lambda x:x+1,list1))
print(list2)
#filter 
list3 = [5,9,2,6,9,5]
listOdd = list(filter(lambda x:x%2 !=0 , list3))
print(listOdd)
#question
allAges = ["5","99","23","9","3","18"]
formattedAllAges = list(map(lambda x:x+" years old",allAges))
"""above18 = list(filter(lambda x:x > 18,formattedAllAges))
print("Total Ages above 18 - ",len(above18))"""
print(formattedAllAges)