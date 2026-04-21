# Todo CLI App

A simple command-line To-Do app built with Python. You can add, view, complete, and delete tasks — all from the terminal. Tasks are saved in a JSON file so they stay even after you close the terminal.

---

## Tech Used

- Python 3
- argparse
- json

---

## Features

- Add tasks
- List all tasks with their status
- Mark a task as done
- Delete a task by ID
- Clear all tasks at once
- Auto-saves to a JSON file

---

## Project Structure

```
todo-cli-app/
├── todo.py
└── todos.json
```

---

## Getting Started

Clone the repo:

```bash
git clone https://github.com/Rajusharma1095/todo-cli-app.git
cd todo-cli-app
```

Run any command:

```bash
python todo.py <command>
```

---

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| list | Show all tasks | python todo.py list |
| add | Add a new task | python todo.py add Buy milk |
| done | Mark task as done | python todo.py done 1 |
| delete | Delete a task | python todo.py delete 2 |
| clear | Delete all tasks | python todo.py clear |

---

## Example Usage

```bash
$ python todo.py add Buy groceries
Task added: Buy groceries

$ python todo.py add Submit assignment
Task added: Submit assignment

$ python todo.py list

Your Tasks:
------------------------------
1. Buy groceries --> Pending
2. Submit assignment --> Pending

$ python todo.py done 1
Task 1 marked as completed.

$ python todo.py delete 2
Task 2 deleted.
```

---

## How Data is Stored

Tasks are saved in todos.json like this:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "done": true
    }
]
```

---

## Note

If you want to change where the JSON file is saved, update this line in todo.py:

```python
FILE = "todos.json"
```

---

## Author

Raju Sharma — [@Rajusharma1095](https://github.com/Rajusharma1095)
