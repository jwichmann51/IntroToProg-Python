# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JWichmann, 5/17/2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strTask = '' # The name of the task
strPriority = '' # The value or priority of the task
strChoice = "" # A Capture the user option selection
dicRow = {}    # The Task and Priority will not go into a list but into a dictionary. A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows.  This incudes multiple rows of data.
strData = ""  # A row of text data from the file
strMenu = ""   # A menu of user options
Row = [] # A row of text data from the file
Table = [] # A table of rows


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# reminders:
# -when you read from the text file and display the data on the screen, you want to remove the carriage return (so use the strip function)
# -when you write to the text file, you want to include the carriage return which is + '\n\


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):

        print("Your Current Data Is")
        for objRow in lstTable:
            print(objRow)

        continue
    # Step 4 - Add a new item to the list/Table

    elif (strChoice.strip() == '2'):

        print(" Type in a Task and Priority")
        strTask = str(input(" Enter a Task: "))
        strPriority = str(input(" Enter the Priority: "))
        lstTable.append({"Task": strTask, "Priority": strPriority})

        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        strTask = input("Task to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("row removed")
                print(lstTable, '<< List with Dictionary objects')
            else:
                print("row not found")
                print(lstTable, '<< List with Dictionary objects')
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n') )
        objFile.close()
        print(" Data was saved!")


        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break
    else:
        print(" Please choose only 1, 2, 3, 4, or 5! ")
