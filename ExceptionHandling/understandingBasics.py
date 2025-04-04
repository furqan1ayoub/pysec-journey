"""
🔹TRY EXCEPT
✅ try → Runs the code. If an error occurs, it jumps to except.
✅ except → Handles the error and prevents program crashes.
"""


#	different Errors 

#1) valueError(Wrong Input Type)
try:
    input1 = "hello"
    print('YOUR twice AGE IS - ',2*input1)
except ValueError:print('ENTER A VALID INPUT')  #Ensures only valid numbers are entered

#2)KeyError (MISSING - KEY IN DICTIONARY)
dict1 = {"1":"furqan","2":"rizwan"}
try:
    key1 = "name"
    print(dict1[key1])
except KeyError:print(f'NO KEY {key1} IN THE DICTIONARY  ')   # Prevents crashes when accessing missing keys.

#3) IndexError (List Index Out of Range)
array1 = ["furqan","rizwan"]
try:
    idx = 3
    print(array1[idx])
except IndexError :print("INDEX NOT FOUND ")         #Ensures we access only valid list indexes.


#4) FileNotFoundError (file doesn't exist )
filename = "abcdkdl.txt"
try:
    with open(filename,"r") as file1:
        content = file1.read()
        print(content)
except FileNotFoundError:print('FILE NOT FOUND')       #Prevents crashes when opening missing files.

#5) PermissionError			No Permission to Access File)

try:
    file = open("/root/protected.txt", "w")
except PermissionError:
    print("Permission denied! Cannot write to this file.")  #Useful when dealing with file access permissions.
except FileNotFoundError:print('dont use it in windows/file not found')

#6) OSERROR -> General System Errors
import os
try:
    os.remove("abc.txt")
except OSError:print("File operation failed! Check if the file exists.")  #Helps when performing system-related tasks.


#7) ZERO-DIVISION ERROR

try:
    num = int(input("enter the number to divide 5 by - ")) #put here cause it might raise error-> cause we converting a thing May cause error
    value = 5/num
    print(value)
except ValueError:print("ENTER VALID NUMBER" )
except ZeroDivisionError:print('ZERO DIVISION ERROR')
except Exception as e:print("ERROR - ",e)
finally:
    print("OPERATION COMPLETED...~")

#qs)
while True:
    try:
        number1 = int(input('ENTER THE NUMBER GUESS - '))
        if number1 < 11:
            print('WRONG ! ENTER THE NUMBER GUESS - ')
        else:
            print('correct !!')
            break
    except ValueError:print("ENTER VALID NUMBER ")