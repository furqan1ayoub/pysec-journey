#Write a function to find the max & min in a list -> no use of min & max

#ans

def MinMaxFind(array):
    smaller_no = array[0]
    larger_no = array[0]
    for eachNo in array:
        if eachNo < smaller_no:
            smaller_no = eachNo
        elif eachNo > larger_no: #only this is true if above one isn't satisified = if the no is greater than the Value of Previous smaller_no
            larger_no = eachNo
    print(f"The Largest NO is {larger_no} & LOwest NO is {smaller_no}")
    
MinMaxFind([2,5,5,899,5,235,5])




#list check

def checkPrimeList(lst):
    set1 = set(lst)  # Remove duplicates
    
    for eachNo in set1:
        if eachNo < 2:
            print(f"{eachNo} is not a prime number (less than 2)")
            continue  # Skip to the next number

        isPrime = True  # Reset flag for each number
        
        for i in range(2, int(eachNo ** 0.5) + 1):  # Efficient check
            if eachNo % i == 0:
                isPrime = False
                break  # Exit loop if not prime
        
        if isPrime:
            print(f"{eachNo} is a prime number")
        else:
            print(f"{eachNo} is not a prime number")

# Test case
checkPrimeList([2, 5, 9, 7, 2, 9, 3, 1, 0])


#check if number is  prime no


def checkPrimeNos(*args):
    for eachNO in args:
        isPrime = True
        if eachNO < 2:
            print("less than 2 -not prime")
            continue
        for i in range(2,eachNO):
            if eachNO % i == 0:
                print(f"{eachNO}divisible by {i}")
                isPrime = False
                break
            else:
                isPrime = True
                break
        if isPrime : print(f"{eachNO} - is a Prime NO")
        else:print(f"{eachNO} - is not a Prime NO")
        
checkPrimeNos(23,2,52,5,2,1,0)


#a fucntion to return only even no's from a list => then put it into array

def onlyEvenNos(list2):
    onlyEvenList = []
    for eachNo in list2:
        if eachNo % 2 == 0 :
            onlyEvenList.append(eachNo)
    return onlyEvenList # put this carefully as next codes dont' run So loops too won't run at first iteration 
evenFromArray = onlyEvenNos([2,68,9,7,3,5,2])
print(evenFromArray)