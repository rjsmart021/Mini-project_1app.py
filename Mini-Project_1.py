#Module 2:Mini-Project] To-Do list Application
#User Interface(UI)
# 1. Add a task
    # 2. View tasks
    # 3. Mark a task as complete
    # 4. Delete a task
    # 5. Quit
#2. To do list=


Tasks = ["Dance", "Drive", "Spin"]

def add_task(x):
    try:
        Tasks.append(x)
        print(Tasks)
    except ValueError:
       print("Error")
def view_task(list):
      print(list)
        
def Mark_C_Task(list):
      print('Complete:', list)

def Mark_I_Task():
      print('Incomplete:', list)

def Delete(Y4):
    try:
        Y4 = input("Task to remove")
        Tasks.remove(Y4)
        print(Tasks)
    except ValueError:
        print("Error")
while True:
    response = input("""Welcome to the to do list app!!!! What would you like to do? 
                1.Add a task
                2. View tasks
                3. Mark a task as complete
                4. Delete a task
                5. Quit      
                     """)
    if response == "1":
                add_task(input("input task to add"))
    elif response == "2":
                print(Tasks)
    elif response == "3":
            a = input("If you want to mark a task complete input 1. If you would like to mark a task incomplete input 2       ")
            if a == "1":
                Mark_C_Task(input("input Task in the list named Tasks to mark complete"))
                Yes = input("Do you want to mark the whole list complete? 1.Yes, 2.NO")
                if Yes == "1":
                    Mark_C_Task(Tasks)
                else:
                     pass 
            else:
                a == "2"
                Mark_I_Task(input("input list subsection to mark incomplete"))
    elif response == "4":
                Delete(input("Task"))
    elif response == "5":
            print("You Have chosen to Quit this application")
    else: 
            print("please enter valid response")
    break