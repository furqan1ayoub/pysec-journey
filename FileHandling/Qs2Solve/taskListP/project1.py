#task list & save tasks in the file when confirmed
#define various functions 1) one which stores adds & stores tasks 2) one which removes tasks 3) one which shows in the terminal all task 4) confirm to save in file currrent tasks 5) quit

def addTask(taskList):
    inputTask = input("ENTER TASK TO ADD - ")
    taskList.append(inputTask)
    print("ADDED TASK - ",inputTask)

def formattedTasks(taskList):
        for idx,eachTask in enumerate(taskList):
            print(f"{idx} - {eachTask}")
#2)
def removeTask(taskList):
    if taskList:
        print('REMMBER THE INDEX NO- ')
        print("THE CURRENT TASK LIST IS ")
        formattedTasks(taskList)
        try:
            inputIdx = int(input("ENTER THE INDEX NUMBER TO REMOVE/COMPLETED - "))
            if inputIdx >=0 and inputIdx < len(taskList): #it is more precise & error reducing if idx isn't found...
                removedElement = taskList.pop(inputIdx)
                print('REMOVED - ',removedElement)
                print('New LIST - \n',taskList)
            else:print("INVALID IDX")
        except ValueError:print('ERROR - ENTER VALID IDX TO DELETE ')  	
    else :print('EMPTY TASK LIST !!!')   
#3)
def showTask(taskList):
    print("THIS IS CURRENT TASK LIST - ")
    print(taskList)
    formattedTasks(taskList)

#4) 
def save_to_file_task(taskList):
    if taskList:
        nameInput = input("ENTER THE FILE-NAME TO KEEP(no ext) -  ") + ".txt"
        with open(nameInput,"w") as taskFile:
            for idx,eachTask in enumerate(taskList,start=1):
                taskFile.write(f"Task{idx} - {eachTask}\n")
        print('DONE !!!')
    else :print('EMPTY TASK LIST !!!')  
    
#5) viewTAsk
def viewTasks_from_file():
    try:
        inputFile = input("ENTER THE FILE NAME TO ADD TASKS TO (no ext)").lower() + ".txt"
        with open(inputFile,"r") as fileToRead:
            found_content = False # for no content track -flag
            for eachLine in fileToRead: # this will only run if it has anything in it i.e file has content 
                print(eachLine.strip())
                found_content = True
            if not found_content:print(f"NO CONTENT INSIDE {inputFile}")
    except FileNotFoundError:print("file no found")        
def projectTaskList():
    taskList = []
    print('-----------------WELCOME TO THE GAME--------------------------- ')
    print("Choose Any one of the below Options\n - ")
    options = "Choose - 1) Add and store tasks\n\n2) Remove tasks\n\n3) Display all tasks in the terminal\n\n4) Confirm and save current tasks to file\n\n 5) See Tasks from files\n\n 6) quit or q or exit to Leave \n "
    while True:
        print(options)
        optionInput = input("ENTER THE OPTION - ")
        if optionInput == "1":addTask(taskList)
        elif optionInput == "2":removeTask(taskList)
        elif optionInput == "3":showTask(taskList)
        elif optionInput == "4":
            print("-------------------confirm----------------------")
            print("NOTE - 1) CONFIRM THE TASK SHOULD BE ADDED ALL \n 2) ADD ONLY FILE NAME (NO EXTENSION) ")
            confirmInput = input('CONFIRM y/n - ').lower()
            if confirmInput=="y" and taskList:
                save_to_file_task(taskList)
            else:
                print("NO TASKS or invalid Name")
                return
        elif optionInput == "5": viewTasks_from_file()
        elif optionInput =="q" or optionInput == "exit":
            print('THANKS FOR PLAYING')
            if taskList:
                print('CURRENT TASK LIST IS -',taskList)
                print('\n THANKS FOR PLAYING ')
                break
            else:
                print('\n THANKS FOR PLAYING ')
                break
        else:print("INVALID INPUT ! TRY AGAIN")
projectTaskList()