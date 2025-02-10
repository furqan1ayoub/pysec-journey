import requests

url = "https://www.google.com"

#now in request module we call get function and put parameters as url
#& as it returns a response i.e json/any form of data structure
#we store it in varaible
response = requests.get(url)

#if now response code means the get is a netwrookg kinda fucntion
#if it got response in the data 200 so print sth

#status code -> inner property/key of the data we got
if response.status_code == 200:
    print(response.status_code) #response ka key text


