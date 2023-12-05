import os
def display():
    print("todo list menu :")
    print("1 view task")
    print("2 add task")
    print("3 mark as done")
    print("4 Delete task")
    print("5 Exit:")

def view(tasks):
    if tasks:
        print("tasks:")
        for i,task in emumerate(tasks,i):
            print(f"{i}.{task}")
    else:
        print("no task found!!")

def add(tasks,new_task):
    tasks.append(new_task)
    print("the task is added successfully ")

def mark(tasks,task_index):
    if task_index >= 1 and task_index <= len(tasks):
        task = tasks[task_index-1]
        print(f"markind task '{task}'as done")
    else:
        print("invalid task index")

def delete(tasks,task_index):
    if task_index >= 1 and task_index <= len(tasks):
        task = tasks.pop(task_index-1)
        print(f"deleted task '{task}")
    else:
        print("invalid task index")

def main():
    task =[]
    while True:
        display()
        choice = input("enter your choice :")

        if choice=="1":
            view(tasks)
        elif choice=="2":
            new_task = input("enter the new task :")
            add(tasks,new_task)
        elif choice=="3":
            view(tasks)
            task_index=input("enter the task number to be marked as done :")
            mark(tasks,task_index)
        elif choice=="4":
            view(taks)
            task_index = input("enter the task you want to delete :")
            delete(tasks,task_index)
        elif choice=="5":
            print("exit the to-do list !!")
            break
        else:
            print("invalid choice ! pkease enter the correct choice")

if _name_ == "_main_":
    main()
