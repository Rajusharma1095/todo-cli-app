import argparse
import json

# --------------------------------------------------
# File path where all tasks will be stored as JSON
# --------------------------------------------------
FILE = "/home/raju/python project/TO_DO/todos.json"

# --------------------------------------------------
# Global variables
# tasks   -> stores all tasks in list format
# next_id -> keeps track of next task ID
# --------------------------------------------------
tasks = []
next_id = 1


# ==================================================
# SAVE TASKS TO FILE
# This function writes current task list into JSON file
# ==================================================
def save_tasks():
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
    print("Tasks saved successfully.")


# ==================================================
# LOAD TASKS FROM FILE
# Reads tasks from JSON file if it exists
# Also sets next_id properly
# ==================================================
def load_tasks():
    global tasks, next_id

    try:
        with open(FILE, 'r') as f:
            tasks = json.load(f)

        # If tasks exist, next_id = highest id + 1
        if tasks:
            next_id = max(task['id'] for task in tasks) + 1
        else:
            next_id = 1

        print("Tasks loaded successfully.")

    except FileNotFoundError:
        # If file doesn't exist, start fresh
        tasks = []
        next_id = 1
        print("No task file found. Starting new list.")


# ==================================================
# DISPLAY ALL TASKS
# Shows task id, description and status
# ==================================================
def list_tasks():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    print("-" * 30)

    for task in tasks:
        status = "✓ Done" if task["done"] else "✗ Pending"
        print(f"{task['id']}. {task['description']} --> {status}")


# ==================================================
# ADD NEW TASK
# Creates new task and adds it to list
# ==================================================
def add_task(description):
    global next_id

    task = {
        "id": next_id,
        "description": description,
        "done": False
    }

    tasks.append(task)
    next_id += 1

    print(f"Task added: {description}")


# ==================================================
# MARK TASK AS DONE
# Finds task by ID and marks complete
# ==================================================
def mark_done(task_id):

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task {task_id} marked as completed.")
            return

    print("Task not found.")


# ==================================================
# DELETE SINGLE TASK
# Removes task using task ID
# ==================================================
def delete_task(task_id):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted.")
            return

    print("Task not found.")


# ==================================================
# DELETE ALL TASKS
# Clears complete list and resets ID counter
# ==================================================
def delete_all_tasks():
    global tasks, next_id

    tasks = []
    next_id = 1

    print("All tasks deleted.")


# ==================================================
# MAIN FUNCTION
# Handles command-line arguments
# ==================================================
def main():

    parser = argparse.ArgumentParser(
        description="My To-Do List App",
        epilog="Example: python todo.py add Buy milk"
    )

    # First argument = command
    parser.add_argument(
        "command",
        choices=["list", "add", "done", "delete", "clear"],
        help="Commands: list, add, done, delete, clear"
    )

    # Remaining words after command
    parser.add_argument(
        "args",
        nargs="*",
        help="Extra arguments for command"
    )

    args = parser.parse_args()

    # Load existing tasks first
    load_tasks()

    # ----------------------------------------------
    # LIST COMMAND
    # ----------------------------------------------
    if args.command == "list":
        list_tasks()

    # ----------------------------------------------
    # ADD COMMAND
    # ----------------------------------------------
    elif args.command == "add":

        if not args.args:
            print("Please enter task name.")
        else:
            add_task(" ".join(args.args))
            save_tasks()

    # ----------------------------------------------
    # DONE COMMAND
    # ----------------------------------------------
    elif args.command == "done":

        if not args.args:
            print("Please enter task ID.")
        else:
            try:
                task_id = int(args.args[0])
                mark_done(task_id)
                save_tasks()

            except ValueError:
                print("ID must be a number.")

    # ----------------------------------------------
    # DELETE COMMAND
    # ----------------------------------------------
    elif args.command == "delete":

        if not args.args:
            print("Please enter task ID.")
        else:
            try:
                task_id = int(args.args[0])
                delete_task(task_id)
                save_tasks()

            except ValueError:
                print("ID must be a number.")

    # ----------------------------------------------
    # CLEAR COMMAND
    # ----------------------------------------------
    elif args.command == "clear":

        confirm = input("Delete ALL tasks? (yes/no): ")

        if confirm.lower() == "yes":
            delete_all_tasks()
            save_tasks()
        else:
            print("Cancelled.")


# ==================================================
# Program starts here
# ==================================================
if __name__ == "__main__":
    main()