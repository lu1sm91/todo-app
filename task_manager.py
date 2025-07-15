import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['description']}")

def add_task(tasks):
    task_desc = input("Enter new task: ")
    tasks.append({"description": task_desc, "done": False})
    save_tasks(tasks)
    print("Task added.")

def mark_task_done(tasks):
    list_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
