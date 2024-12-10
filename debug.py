
TASKS_FILE = "tasks.json"
import json
from typing import Optional


def read_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)


def find_task(id, verify: Optional[bool] = True):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == id:
            if verify:
                return True
            return task


if __name__ == "__main__":
    print(find_task(3))