#lambda functions
#small and anonymous function / short iners for short and quick using ops

x = lambda x : x+50
print(x(5))


#map -> for each iteratble it does some ops on it and returns and we store it 
#using it with lamda is best

list1 = [2,5,9,2,5,5]
even_nos = map(lambda x : x*x, list1)
print(list(even_nos))


# hacking use case

payloads = ["admin","root","user"]
encoded_payloads = list(map(lambda x : x.upper() , payloads))
print(encoded_payloads)


#filter -> only gives/returns based on the codintios same => put into the return nos into list/tuple

list2 = [2,5,9,5,73,5,2]
even_nos = list(set(filter(lambda x : x % 2 == 0 , list2)))
print(even_nos) # only [2]

#hacking usecase

urls = ["eg.com/user2", "eg2.com/admin", "eg3.com/user1","eg.come/user5"]

result = list(filter(lambda x : "admin" in x , urls))
print(result) #only admin wala url