import click
import csv
import time

tasks = []

@click.command()
def menu():
    


    click.echo("\nCHOICES:")
    click.echo("---------")
    click.echo("\n(C)........Create a task.")
    click.echo("\n(D)........Delete a task.")
    click.echo("\n(S)........Start timing a task.")
    click.echo("\n(P)........Stop timing a task.")
    click.echo("\n(F)........Export timesheet as CVS file.")
    click.echo("\n(E)........Exit.")
    click.echo("\nInput the indicated letter for the option you wish to select: ")

    choice = input()

    if choice == 'C':
        create_task()

    elif choice == 'D':
        delete_task()

    elif choice == 'S':
        start_timer()

    elif choice == 'P':
        stop_timer()

    elif choice == "F":
        export_as_cvs_file()

    elif choice == 'E':
        exit()


def create_task():

    task_name = input("\nCreate a task: ")
    tasks.append({"name": task_name, "status": None, "time_taken": None})

    show_tasks()


def delete_task():

    index = int(input("\nEnter the task number you wish to delete: ")) - 1
    tasks.pop(index)

    show_tasks()

@click.command()
def start_timer():
    start_choice = (int(input("\nEnter the task number you wish to start timing: "))) - 1

    tasks[start_choice]["status"] = time.time()

    click.echo(f"Timer for {tasks[start_choice]["name"]} started!")

    show_tasks()
    
@click.command()
def stop_timer():
    stop_choice = (int(input("\nEnter the task number you wish to stop timing: "))) - 1

    start_time = tasks[stop_choice]["status"]
    elapsed_time = time.time() - start_time
    mins, secs = divmod(int(elapsed_time), 60)
    tasks[stop_choice]["status"] = "Complete"
    tasks[stop_choice]["time_taken"] = f"00:00 to {mins:02}:{secs:02}"

    click.echo(f"\nTask '{tasks[stop_choice]["name"]}' is now stopped.")
    click.echo(f"Time of Task -> 00:00 to {mins:02}:{secs:02}")

    show_tasks()


@click.command()
def export_as_cvs_file():

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

    click.echo(f"\nTimsheet exported!")

    return menu()

@click.command()
def show_tasks():

    click.echo("\nTASKS:")
    click.echo("-------")

    for i, task in enumerate(tasks, start=1):

        if task["status"] == "Complete":
            timer_status = "Complete"
        elif task["status"]:
            timer_status = "Currently Running"
        else:
            timer_status = "Timer Not Started"

        click.echo(f"{i}. {task['name']} -> {timer_status}")
    
    return menu()


def main():
        
    menu()
    

if __name__ == '__main__':
    main()