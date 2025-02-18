""" 
main.py
Abe Gomez <abraham.gomez@student.cune.edu>
This module holds the main code for this Python Task Timer Project.
"""


import csv
from datetime import datetime
import pytz
import shutil

central_time = pytz.timezone("US/Central")

def menu():
    """ Allow the user to manipulate the task timer. """

    print("\nCHOICES:")
    print("---------")
    print("\n(C)........Create a task.")
    print("\n(D)........Delete a task.")
    print("\n(S)........Start timing a task.")
    print("\n(P)........Stop timing a task.")
    print("\n(T)........Print/Show current task list/timesheet.")
    print("\n(F)........Export timesheet as CSV file.")
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
            export_as_csv_file()

        elif choice == 'E':
            exit()

        else:
            print("Invalid input. Please try again.")



def create_task():
    """ Input task into task list. """

    task_name = input("\nCreate a task: ")

    task_data = {"name": task_name, "status": "Task Not Started", "time_taken": "N/A"}

    with open("timesheet.csv", mode="a", newline="") as csvfile:
        fieldnames = ['name', 'status', 'time_taken']
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)        
        thewriter.writerow(task_data)

    print(f"\nTask '{task_name}' has been created!")

    show_tasks()


def delete_task():
    """ Remove a task from the task list. """

    task_to_delete = input("\nEnter the task name you wish to delete: ")
    kept_tasks = []
    task_found = False

    with open("timesheet.csv", mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["name"] != task_to_delete:
                kept_tasks.append(row)

            else:
                task_found = True
    
    if not task_found:
        print(f"\nNo task with the name '{task_to_delete}' found.")
        delete_task()
    
    else:
        with open("timesheet.csv", mode="w", newline="") as csvfile:
            fieldnames = ['name', 'status', 'time_taken']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

            thewriter.writeheader()
            thewriter.writerows(kept_tasks)

        print(f"\nTask '{task_to_delete}' has been deleted!")

        show_tasks()



def start_timer():
    """ Begin the timer on a specific task chosen by the user. """

    started_task = (input("\nEnter the task name you wish to start timing: "))
    updated_tasks = []
    task_found = False

    with open("timesheet.csv", mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["name"] == started_task:
                row["status"] = "Currently Running"
                start_time = datetime.now(central_time)
                row["time_taken"] = start_time.strftime("%m-%d-%Y %I:%M:%S:%p")
                updated_tasks.append(row)
                task_found = True
            
            else:
                updated_tasks.append(row)
    
    if not task_found:
        print(f"\nNo task with the name '{started_task}' found.")
        start_timer()
    
    else:
        with open("timesheet.csv", mode="w", newline="") as csvfile:
            fieldnames = ['name', 'status', 'time_taken']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

            thewriter.writeheader()
            thewriter.writerows(updated_tasks)

        print(f"\nTask '{started_task}' has been started!")

        show_tasks()


def stop_timer():
    """ Stop the timer on a specific task chosen by the user. """

    stopped_task = (input("\nEnter the task name you wish to stop timing: "))
    updated_tasks = []
    task_found = False


    with open("timesheet.csv", mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["name"] == stopped_task:
                row["status"] = "Task Finished"

                start_time_str = row["time_taken"]
                start_time = datetime.strptime(start_time_str, "%m-%d-%Y %I:%M:%S:%p")
                start_time = central_time.localize(start_time)
                start_time = start_time.replace(microsecond=0)

                end_time = datetime.now(central_time)
                end_time = end_time.replace(microsecond=0)

                elapsed_time = end_time - start_time

                total_seconds = elapsed_time.total_seconds()

                hours, remainder = divmod(total_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                formatted_elapsed_time = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
                row["time_taken"] = formatted_elapsed_time

                updated_tasks.append(row)
                task_found = True
            
            else:
                updated_tasks.append(row)
    
    if not task_found:
        print(f"\nNo task with the name '{stopped_task}' found.")
        stop_timer()
    
    else:
        with open("timesheet.csv", mode="w", newline="") as csvfile:
            fieldnames = ['name', 'status', 'time_taken']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

            thewriter.writeheader()
            thewriter.writerows(updated_tasks)

        print(f"\nTask '{stopped_task}' has been stopped! It took {elapsed_time} (hours:min:sec).")

        show_tasks()


def export_as_csv_file():
    """ Export timesheet (task list) to a desired CVS file. """

    desired_file = input("\nCreate a filename you wish to export the time sheet to. Please add .csv to the end of the filename: ")
    shutil.copy("timesheet.csv", desired_file)

    print(f"\nTimsheet exported!")

    return menu()


def show_tasks():
    """ Print the current task list. """

    print("\nTASKS:")
    print("-------")

    with open("timesheet.csv", mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            print(f"Task: {row['name']}, Status: {row['status']}, Time Taken: {row['time_taken']}")

    return menu()

def create_timesheet():
    """ Create the timesheet file that the user will be modifying. """

    with open("timesheet.csv", mode="w", newline="") as csvfile:
        fieldnames = ['name', 'status', 'time_taken']

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()
        


def main():
    """ Operate the task timer and its functions. """

    create_timesheet()
    menu()
    

if __name__ == '__main__':
    main()