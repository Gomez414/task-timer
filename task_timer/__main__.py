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

    if choice == 'D':
        delete_task()

    if choice == 'S':
        start_timer()

    if choice == 'P':
        stop_timer()

    if choice == "F":
        export_as_cvs_file()

    if choice == 'E':
        exit()


def create_task():

    task_name = input("\nCreate a task: ")
    tasks.append({"name": task_name, "status": None})

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
    tasks[stop_choice]["status"] = None

    click.echo(f"\nTask '{tasks[stop_choice]["name"]}' is now stopped.")
    click.echo(f"Elapsed Time of Task -> {mins:02}:{secs:02}")

    show_tasks()


def export_as_cvs_file():

    with open('timesheet.csv', 'w', newline='') as csvfile:

        fieldnames = ['name', 'status']

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()

        for task in tasks:
            thewriter.writerow({'name': task, 'status': tasks[task]["status"]})

    return menu()

@click.command()
def show_tasks():

    click.echo("\nTASKS:")
    click.echo("-------")

    for i, task in enumerate(tasks, start=1):
        if task["status"]:
            timer_status = "Currently Running"
        else:
            timer_status = "Timer Not Started"

        click.echo(f"{i}. {task['name']} -> {timer_status}")
    
    return menu()


def main():
        
    menu()
    

if __name__ == '__main__':
    main()