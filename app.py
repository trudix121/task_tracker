import click
import json
from datetime import datetime

# Numele fișierului JSON
TASKS_FILE = "tasks.json"

# Inițializarea fișierului JSON dacă nu există
def initialize_tasks_file():
    try:
        with open(TASKS_FILE, 'x') as file:
            json.dump([], file)
    except FileExistsError:
        pass
    
def find_task_by_desc(desc):
    tasks = read_tasks()
    for task in tasks:
        if task["description"] == desc:
            return task
    return None


def update_task_description(task_id, new_description):
    tasks = read_tasks()  # Citim task-urile existente
    task_found = False

    for task in tasks:
        if task["id"] == task_id:  # Găsim task-ul după ID
            task["description"] = new_description  # Actualizăm descrierea
            task["updated_at"] = datetime.now().strftime('%Y-%m-%d')  # Actualizăm timestamp-ul
            task_found = True
            break

    if task_found:
        write_tasks(tasks)  # Salvăm modificările în fișier
        print(f"Task-ul cu ID-ul {task_id} a fost actualizat cu succes.")
    else:
        print(f"Niciun task cu ID-ul {task_id} nu a fost găsit.")

# Funcție pentru a citi task-urile existente din fișier
def read_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Funcție pentru a scrie task-urile în fișier
def write_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Grupul principal de comenzi
@click.group()
def cli():
    """Task Manager CLI"""
    initialize_tasks_file()

# Comanda pentru a adăuga un task
@cli.command()
@click.argument('name')
def add(name):
    """Adaugă un task nou."""
    if not name:
        click.echo("Numele task-ului este obligatoriu!")
        return
    if find_task_by_desc(name):
        click.echo("Task-ul există deja!")
        return
    try:
        # Crearea unui task nou
        task = {
            "id": None,
            "description": name,
            "status": "to-do",
            "created_at": datetime.now().strftime('%Y-%m-%d'),
            "updated_at": datetime.now().strftime('%Y-%m-%d')
        }

        # Citirea task-urilor existente și adăugarea celui nou
        tasks = read_tasks()
        task["id"] = len(tasks) + 1  # Generare automată ID
        tasks.append(task)

        # Salvarea task-urilor în fișier
        write_tasks(tasks)

        click.echo(f"The task '{task['description']}' was added successfully. (ID: {task['id']})")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
@cli.command()
@click.argument('id', type=int)
@click.argument('description', type=str)
def update(id, description):
    if not id and description:
        click.echo("Id and description are required!")
        return
    else:
        update_task_description(id, description)
        
if __name__ == "__main__":
    cli()
