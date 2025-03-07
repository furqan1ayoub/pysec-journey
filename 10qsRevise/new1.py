import time
user = ["admin","user1234","furqann8"]
pwd = ["abcd","instagram123","honeysingh"]
for i in user:
    LoggedIn = False
    for y in pwd:
        print(f"{i} - {y}")
        time.sleep(0.5)
        if i=="admin" and y=="honeysingh":
            print(f"SUCCESS {i} - {y}")
            LoggedIn = True
            break
    if(LoggedIn == True):break
    
    

                
    
            