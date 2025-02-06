import click
import csv
import time

@click.command()
def menu():

    click.echo("\nCHOICES:")
    click.echo("---------")
    click.echo("\n(C)........Create a task.")
    click.echo("\n(D)........Delete a task.")
    click.echo("\n(S)........Start timing a task.")
    click.echo("\n(P)........Stop timing a task.")
    click.echo("\n(E)........Exit.")
    click.echo("\n(F)........Export timesheet as CVS file.")
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

@click.command()
def create_task():

    create = input("\nCreate a task: ")
    tasks.append(create)


    click.echo("\nTASKS:")
    click.echo("-------")

    for i, item in enumerate(tasks, start=1):
        click.echo(f"{i}. {item}")

    return menu()

@click.command()
def delete_task():

    index = int(input()) - 1
    tasks.pop(index)

    for i, item in enumerate(tasks, start=1):
        click.echo(f"{i}. {item}")

@click.command()
def start_timer():
    task_choice = input("/nEnter the name of the task you wish to start: ")

    tasks[task_choice] = time.time()

    click.echo(f"{task_choice} started at {tasks}")
    

def stop_timer():



def export_as_cvs_file():

    with open('timesheet.csv', 'w', newline='') as csvfile:

        fieldnames = ['task_name', 'start_time', 'status']

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()

        for task in tasks:
            thewriter.writerow({'task_name': task })

    return menu()



tasks = []

@click.command()
def main():
    """This is my main cli."""
        
    menu()
    

if __name__ == '__main__':
    main()