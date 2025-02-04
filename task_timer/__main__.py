import click

@click.command()
def menu():

    click.echo("\nCHOICES:")
    click.echo("---------")
    click.echo("\n(C)........Create a task")
    click.echo("\n(D)........Delete a task")
    click.echo("\n(E)........Exit")
    click.echo("\nInput the indicated letter for the option you wish to select: ")

    choice = input()

    if choice == 'C':
        create_task()

    if choice == 'D':
        delete_task()

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




tasks = []

@click.command()
def main():
    """This is my main cli."""

    menu()
    

if __name__ == '__main__':
    main()