import subprocess
import sys


# Function to check and install missing libraries
def install_libraries():
    try:
        import click
        import json
        import datetime
    except ModuleNotFoundError:
        print("Some libraries are missing, installing them...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        print("Libraries installed. Please try running the script again.")
        sys.exit(1)

# Check and install libraries if missing
install_libraries()

import click
import json
from datetime import datetime
from typing import Optional

TASKS_FILE = "tasks.json"

def initialize_tasks_file():
    try:
        with open(TASKS_FILE, 'x') as file:
            json.dump([], file)
    except FileExistsError:
        pass

def read_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def write_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def find_task_by_desc(desc):
    tasks = read_tasks()
    return next((task for task in tasks if task["description"] == desc), None)

def find_task(id, verify: Optional[bool] = True):
    tasks = read_tasks()
    return next((task for task in tasks if task["id"] == id), None) if verify else True

def remove_task_by_id(task_id):
    tasks = read_tasks()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        tasks.remove(task)
        write_tasks(tasks)
        return f"Task with ID {task_id} has been deleted."
    return f"No task with ID {task_id} found."

def update_task_status(task_id: int, status):
    tasks = read_tasks()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        if task["status"] == status:
            return print(f"This task is already marked as {status}")
        task["status"] = status
        task["updated_at"] = datetime.now().strftime('%Y-%m-%d')
        write_tasks(tasks)
        print(f"Task with ID {task_id} has been updated successfully.")
    else:
        print(f"No task with ID {task_id} found.")

def update_task_description(task_id, new_description):
    tasks = read_tasks()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["description"] = new_description
        task["updated_at"] = datetime.now().strftime('%Y-%m-%d')
        write_tasks(tasks)
        print(f"Task with ID {task_id} has been updated successfully.")
    else:
        print(f"No task with ID {task_id} found.")

@click.group()
def cli():
    initialize_tasks_file()

@cli.command()
@click.argument('name')
def add(name):
    if not name:
        click.echo("Task name is required!")
        return
    if find_task_by_desc(name):
        click.echo("Task already exists!")
        return
    tasks = read_tasks()
    max_id = max((task["id"] for task in tasks), default=0)
    task = {
        "id": max_id + 1,
        "description": name,
        "status": "to-do",
        "created_at": datetime.now().strftime('%Y-%m-%d'),
        "updated_at": datetime.now().strftime('%Y-%m-%d')
    }
    tasks.append(task)
    write_tasks(tasks)
    click.echo(f"The task '{task['description']}' was added successfully. (ID: {task['id']})")

@cli.command()
@click.argument('id', type=int)
@click.argument('description', type=str)
def update(id, description):
    if id and description:
        update_task_description(id, description)

@cli.command()
@click.argument('id', type=int)
def remove(id):
    click.echo(remove_task_by_id(id))

@cli.command()
@click.argument('id', type=int)
def mark_in_progress(id):
    update_task_status(id, "in-progress")

@cli.command()
@click.argument('id', type=int)
def mark_done(id):
    if input("Do you want to mark this task as done and delete it? (y/n): ").lower() == 'y':
        print(remove_task_by_id(id))
        print("Task deleted successfully. Great work! :)")
    else:
        update_task_status(id, "done")

@cli.command()
@click.argument('status', type=str, required=False)
def list(status):
    tasks = read_tasks()
    filtered_tasks = [task for task in tasks if status is None or task['status'] == status]
    if filtered_tasks:
        click.echo(f"Task List ({status if status else 'All'}):")
        for task in filtered_tasks:
            click.echo(f"{task['id']}. {task['description']} (Status: {task['status']}, Created: {task['created_at']}, Updated: {task['updated_at']})")
    else:
        click.echo(f"No tasks found with status '{status}'." if status else "No tasks available.")

if __name__ == "__main__":
    cli()
