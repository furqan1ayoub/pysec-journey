# get the ERROR lines pattern and save to file named onlyError.txt

def addTofile(eachLine,newFileToAdd):
    try:
        with open(newFileToAdd,"a") as file2:
            file2.write(f"{eachLine} \n")
    except ValueError:print('NAME ERROR')
    except FileExistsError:print('FILE ALREADY EXISTS')
    except Exception as e:print(f"ERROR - {e}")
def fileanalyzer(filename):
    newFileToAdd= input("ENTER THE FILE-NAME TO KEEP(without-ext) ") + ".txt"
    try:
        with open(newFileToAdd,"w") as file2:
            pass # Clear file before writing new errors
        # this is for analaying the file
        with open(filename,"r") as file1:
            for eachLine in file1:
                if "ERROR" in eachLine:
                    print(eachLine)
                    addTofile(eachLine,newFileToAdd)
    except FileNotFoundError:print('FILE NOT FOUND')

if __name__ == "__main__":
    fileanalyzer("file1.txt")