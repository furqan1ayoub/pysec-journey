# A while loop
**in Python repeatedly executes a block of code as long as a specified condition is True. It’s useful when you don’t know beforehand how many times you need to run the loop.**

```python
Basic Syntax:

while condition:
    # Code to execute
	#if some conditon true:
		#do this 
		#break
	
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
Output:

Count is: 0  
Count is: 1  ............

#sum upto a unpredicatble input of the user
a = int(input("Enter the no - "))
sum = 0
while True:
    if a != 0:
        sum += a
        a = int(input("Enter Next No. to Add "))
        print("PRESS 0 to Exit ")
    elif a == 0:
        print("The Sum of Numbers - ", sum)
        break


```
# How It Helps in Hacking (Your Goal):
1) Brute Force Attacks: Automate password guessing by repeatedly trying combinations until success.
2) Network Scanning: Continuously scan ports or devices until a condition is met.
3) Script Automation: Keep scripts running to monitor logs or system behavior.