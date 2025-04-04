#do basic dir enumeration & save the correct and found -> in file
import requests

def save_to_file(newDirFile,full_url):
    try:
        with open(newDirFile,"a") as newFile:
            newFile.write(f"{full_url}\n")
    except ValueError:print('ENTER VALID NAME ')
    except Exception as e :print('ERROR ',e)
def dirEnumerator(url, filename):
    try:
        with open(filename, "r") as dirFile:
            newDirFile = input("Enter the filename to save found paths (no ext): ") + ".txt" #for only calling once 
            with open(newDirFile,"w") as newFile:
                tabs = "\t"*10 #just spacing and making heading clear
                newFile.write(f"{tabs}WORKING LINKS / DIRECOTIRES \n")
            for eachLine in dirFile:
                eachLine = eachLine.strip() # for whitespace remove
                if eachLine and eachLine[0] == "/": # to check eachline has sth in it
                    
                    # add now the dir & make full url to try
                    full_url = url.rstrip("/") +"/" + eachLine.strip().lstrip("/") #add (impt), rstip-> is kinda removes the last rstrip
                    try:
                        response = requests.get(full_url)
                        if response.status_code == 200:
                            print(f"FOUND - {eachLine} {[response.status_code]} ",)\
                            #call
                            save_to_file(newDirFile,full_url)
                        elif response.status_code in [301,302]: 
                            print(f"REDIRECTED - {eachLine} {response.status_code}")
                        else:print(f"NOT FOUND - {eachLine} {response.status_code}")
                    except requests.RequestException as e :
                        print(f"Error - {e}")
    except FileNotFoundError:
        print("FILE NOT FOUND")
    except Exception as e:
        print("error -->", e)

if __name__ == "__main__":
    dirEnumerator("http://localhost:80", "dirFile.txt")
    print("DONE !!")