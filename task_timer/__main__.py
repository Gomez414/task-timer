""" 
main.py
Abe Gomez <abraham.gomez@student.cune.edu>
This module holds the main code for this Python Task Timer Project.
"""


import csv
from datetime import datetime

tasks = []

def menu():
    """ Allow the user to manipulate the task timer. """

    print("\nCHOICES:")
    print("---------")
    print("\n(C)........Create a task.")
    print("\n(D)........Delete a task.")
    print("\n(S)........Start timing a task.")
    print("\n(P)........Stop timing a task.")
    print("\n(T)........Print/Show current task list/timesheet.")
    print("\n(F)........Export timesheet as CVS file.")
    print("\n(E)........Exit.")
    print("\nInput the indicated letter for the option you wish to select: ")

    while True:
        choice = input()

        if choice == 'C':
            create_task()

        elif choice == 'D':
            delete_task()

        elif choice == 'S':
            start_timer()

        elif choice == 'P':
            stop_timer()

        elif choice == 'T':
            show_tasks()

        elif choice == "F":
            export_as_cvs_file()

        elif choice == 'E':
            exit()

        else:
            print("Invalid input. Please try again.")



def create_task():
    """ Input task into task list. """

    task_name = input("\nCreate a task: ")
    tasks.append({"name": task_name, "status": None, "time_taken": None})

    show_tasks()


def delete_task():
    """ Remove a task from the task list. """

    while True:
        try:
            index = int(input("\nEnter the task number you wish to delete: ")) - 1
            tasks.pop(index)
            show_tasks()
        
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        except IndexError:
            print("Invalid task number. Please enter a number in the list.")



def start_timer():
    """ Begin the timer on a specific task chosen by the user. """

    while True:
        try:
            start_choice = (int(input("\nEnter the task number you wish to start timing: "))) - 1

            tasks[start_choice]["status"] = datetime.now()

            print(f"Timer for {tasks[start_choice]["name"]} started!")

            show_tasks()

        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        except IndexError:
            print("Invalid task number. Please enter a number in the list.")


def stop_timer():
    """ Stop the timer on a specific task chosen by the user. """

    while True:
        try:
            stop_choice = (int(input("\nEnter the task number you wish to stop timing: "))) - 1

            start_time = tasks[stop_choice]["status"]
            elapsed_time = datetime.now() - start_time
            elapsed_seconds = int(elapsed_time.total_seconds())
            mins, secs = divmod(elapsed_seconds, 60)
            tasks[stop_choice]["status"] = "Complete"
            tasks[stop_choice]["time_taken"] = f"00:00 to {mins:02}:{secs:02}"

            print(f"\nTask '{tasks[stop_choice]["name"]}' is now stopped.")
            print(f"Time of Task -> 00:00 to {mins:02}:{secs:02}")

            show_tasks()

        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        except IndexError:
            print("Invalid task number. Please enter a number in the list.")


def export_as_cvs_file():
    """ Export timesheet (task list) to a CVS file. """

    with open('timesheet.csv', 'w', newline='') as csvfile:

        fieldnames = ['name', 'status', 'time']

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()

        for task in tasks:

            if task["status"] == "Complete":
                timer_status = "Complete"
            elif task["status"]:
                timer_status = "Currently Running"
            else:
                timer_status = "Timer Not Started"
            
            thewriter.writerow({'name': task["name"], 'status': timer_status, 'time':task["time_taken"]})

    print(f"\nTimsheet exported!")

    return menu()


def show_tasks():
    """ Print the current task list. """

    print("\nTASKS:")
    print("-------")

    for i, task in enumerate(tasks, start=1):

        if task["status"] == "Complete":
            timer_status = "Complete"
        elif task["status"]:
            timer_status = "Currently Running"
        else:
            timer_status = "Timer Not Started"

        print(f"{i}. {task['name']} -> {timer_status}")
    
    return menu()


def main():
    """ Operate the task timer and its functions. """

    menu()
    

if __name__ == '__main__':
    main()