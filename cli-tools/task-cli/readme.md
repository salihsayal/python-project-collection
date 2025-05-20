# Task Tracker CLI

A simple command-line application to track your tasks and manage your to-do list. This tool helps you add, update, mark, and list tasks using a local JSON file for persistent storage.

## Features

- Add, update, and delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- List:
  - All tasks
  - Only completed tasks
  - Only tasks in progress
  - Only tasks not done
- Automatically saves tasks to a JSON file in the current directory

## Usage

Run the CLI with the following commands:

### Add a Task

```bash
    ./task-cli add "Buy groceries"
    # Output: Task added successfully (ID: 1)
```

### Update or Delete a Task
```bash
    ./task-cli update 1 "Buy groceries and cook dinner"
    ./task-cli delete 1
```

### Mark Task as In Progress or Done
```bash
    ./task-cli mark-in-progress 1
    ./task-cli mark-done 1
```

### List Tasks
```bash
    ./task-cli list            # List all tasks
    ./task-cli list done       # List completed tasks
    ./task-cli list todo       # List pending tasks
    ./task-cli list in-progress # List in-progress tasks
```

## Task Properties
Each task in the JSON file includes the following:
- `id`: A unique task identifier
- `description`: A short description of the task
- `status`: One of `todo`, `in-progress`, or `done`
- `createdAt`: Timestamp when the task was created
- `updatedAt`: Timestamp when the task was last modified

## Installation
No external libraries required – uses only the standard library.
Make sure to run the script with Python 3 installed. 

## Notes
- Tasks are stored in a `tasks.json` file in the current working directory.
- The file is created automatically if it doesn't exist.
- Ensure graceful handling of invalid inputs and edge cases.
