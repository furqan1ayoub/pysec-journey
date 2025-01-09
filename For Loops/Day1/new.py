#A                   Sum of Numbers: Write a program to calculate the sum of all numbers from 1 to 150 using a loop.
#ans
#psudeo code:-

#1)create a sum variable where we put value = 0 to store the iterator value like a box that keeps on adding when anything adds
sum = 0
#2)use for loop 
for i in range(1,151):
    print(i) #we print all iterator value 
    
#3) store i value each time in a box i.e sum variable which keeps on adding until i=100 / loop ends
    sum+=i #or sum = sum+i(same)

#5)we now after the above loop ends print the value of sum i.e

print(sum)#result - 11325

#B                 Even Numbers: Write a program to print all even numbers from 1 to 50 using a loop.

#ans

#1) it is easy as we have to apply only on for loop and in it Conditional statements - So adding sum too
sumEvenNO = 0

for i in range(71):
    if(i%2==0):
        print(i)
        #2)kinda same as above but here only due to conditional statements -> only even no's to add in a box....!
        sumEvenNO+=i
print(sumEvenNO) #result -> 1260.



#-----------------------------------------------------------------------------well done---------------------------------------------------------------