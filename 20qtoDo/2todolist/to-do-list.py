# To-Do List

# 1st Step: Define a Data Storage
all_tasks = []

# Add Task Function
def addtask():
    inputAdd = input("Enter The Task To Add - ")
    print("Added Task - ", inputAdd)
    all_tasks.append(inputAdd)

# View Tasks Function
def viewtask():
    if not all_tasks:print("No Tasks added- ")
    else:
        print("All Tasks:")
        for idx, task in enumerate(all_tasks):
        	print(f"{idx}) {task}")

# Delete Task Function
def deleteTask():
    print("Remember The idx/Task-No to Delete that Task")
    for idx, eachTask in enumerate(all_tasks):
        print(idx, eachTask)
    try:#for if there input is alphabet will save from converting error
        Inputidx = int(input("- Enter The Task No to Delete - "))
        if 0 <= Inputidx < len(all_tasks): #for if there isn't the idx in the list
            removed_task = all_tasks.pop(Inputidx)
            print("Deleted Task -", removed_task)
            print("New-List \n", all_tasks)
        else:
            print("INCORRECT TASK NO")
    except ValueError:
        print("Please enter a valid number.")

# Mark Task as Done
def donetask():
    print("Remember The idx/Task-No Completed - ")
    for idx, eachTask in enumerate(all_tasks):
        print(idx, eachTask)
    try:
        Inputidx = int(input("- Enter The Task No Done - "))
        if 0 <= Inputidx < len(all_tasks):
            removed_task = all_tasks.pop(Inputidx) #pop more efficinet than remove as it remove by idx which is needed here..
            print("Done & Removed Task -", removed_task)
            print("New-List \n", all_tasks)
        else:
            print("INCORRECT TASK NO")
    except ValueError:
        print("Please enter a valid number.")

# Main Loop
while True:
    print('WELCOME TO TO-DO-LIST \n CHOOSE ONE OF THE OPTIONS')
    print('1) add a task \n 2) view all tasks \n 3) delete a task \n 4) Completed a task \n 5) press q or 5 to leave')
    userInput = input("ENTER YOUR OPTION - ")
    if userInput == "1": addtask()
    elif userInput == "2": viewtask()
    elif userInput == "3": deleteTask()
    elif userInput == "4": donetask()
    elif userInput == "q" or userInput == "5":
        print("THANKS FOR USING")
        print("ALL TASKS LEFT: \n")
        viewtask()
        break
