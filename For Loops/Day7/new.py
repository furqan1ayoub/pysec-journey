#Do if have time- mutliplication of numbers upto that no say if 10 is no 1 to 10 multplication tables 
# using netsted loop(do either for improving  logic or do at end)

#normal printing in
for y in range(1,10):
    for x in range(1,11):
        print(f"{y}*{x} = {y*x}")
    print()#just space at b/w each table


#put all tables in a row
for x in range(1,11):#acting here as mutlipliers
    for y in range(1,10): #acting here as no
        print(f"{y} * {x} = {x*y}",end="\t") #this will be like 1*1 2*1 3*1....2nd row 1*2 2*2 3*2.......likewise at each row ! no next line but tab....
        #understand the above to get all...
    print()#on every inner loops exit start new loop in next line 