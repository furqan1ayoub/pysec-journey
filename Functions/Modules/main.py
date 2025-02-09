import greetings
print(greetings.greetFunc()) #the value is used here

print("This is not that function We imported here the function ")

import math

print(math.sqrt(16)) #this is a function in the math defined once we just used it anywhere...


import requests
url = "https://www.gandhicollegesrinagar.edu.in"

response = requests.get(url) #here we call from request a get function which returns the result and we store it and contains various properties
print(response.status_code) #print the response objects-> status code property value
#200
