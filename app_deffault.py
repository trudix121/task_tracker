import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def initialize_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w+') as file:
            json.dump([], file)

def read_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def write_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def find_task_by_desc(desc):
    tasks = read_tasks()
    for task in tasks:
        if task["description"] == desc:
            return task
    return None

def remove_task_by_id(task_id):
    tasks = read_tasks()
    task_found = False
    for task in tasks[:]:
        if task["id"] == task_id:
            tasks.remove(task)
            task_found = True
            break
    if task_found:
        write_tasks(tasks)
        return f"Task with ID {task_id} was deleted."
    else:
        return f"No task with ID {task_id} found."

def update_task_status(task_id, status):
    tasks = read_tasks()
    task_found = False
    for task in tasks:
        if task["status"] == status:
            return f"This task is already marked as {status}"
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().strftime('%Y-%m-%d')
            task_found = True
            break
    if task_found:
        write_tasks(tasks)
        return f"Task with ID {task_id} was updated successfully."
    else:
        return f"No task with ID {task_id} found."

def update_task_description(task_id, new_description):
    tasks = read_tasks()
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = datetime.now().strftime('%Y-%m-%d')
            task_found = True
            break
    if task_found:
        write_tasks(tasks)
        return f"Task with ID {task_id} was updated successfully."
    else:
        return f"No task with ID {task_id} found."

def find_task(id, verify=True):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == id:
            if verify:
                return True
            return task

def add_task(name):
    if not name:
        return "Task name is required!"
    if find_task_by_desc(name):
        return "Task already exists!"
    tasks = read_tasks()
    max_id = max(task["id"] for task in tasks) if tasks else 0
    task = {
        "id": max_id + 1,
        "description": name,
        "status": "to-do",
        "created_at": datetime.now().strftime('%Y-%m-%d'),
        "updated_at": datetime.now().strftime('%Y-%m-%d')
    }
    tasks.append(task)
    write_tasks(tasks)
    return f"Task '{task['description']}' added successfully. (ID: {task['id']})"

def list_tasks(status=None):
    tasks = read_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
        if tasks:
            result = f"Task List ({status}):\n"
            for task in tasks:
                result += f"{task['id']}. {task['description']} (Created: {task['created_at']}, Updated: {task['updated_at']})\n"
            return result
        else:
            return f"No tasks found with status '{status}'."
    else:
        result = "Task List:\n"
        for task in tasks:
            result += f"{task['id']}. {task['description']} (Status: {task['status']}, Created: {task['created_at']}, Updated: {task['updated_at']})\n"
        return result

if __name__ == "__main__":
    initialize_tasks_file()

    while True:
        print("\nCommands:")
        print("1. add <task_name>")
        print("2. remove <task_id>")
        print("3. update <task_id> <new_description>")
        print("4. mark_done <task_id>")
        print("5. mark_in_progress <task_id>")
        print("6. list [done/in-progress]")

        command = input("Enter command: ").split()
        if not command:
            continue

        action = command[0]
        if action == "add" and len(command) > 1:
            task_name = ' '.join(command[1:])
            print(add_task(task_name))

        elif action == "remove" and len(command) == 2:
            task_id = int(command[1])
            print(remove_task_by_id(task_id))

        elif action == "update" and len(command) == 3:
            task_id = int(command[1])
            new_description = command[2]
            print(update_task_description(task_id, new_description))

        elif action == "mark_done" and len(command) == 2:
            task_id = int(command[1])
            print(update_task_status(task_id, "done"))

        elif action == "mark_in_progress" and len(command) == 2:
            task_id = int(command[1])
            print(update_task_status(task_id, "in-progress"))         

        elif action == "list":
            status = command[1] if len(command) > 1 else None
            print(list_tasks(status))
        else:
            print("Invalid command.")


