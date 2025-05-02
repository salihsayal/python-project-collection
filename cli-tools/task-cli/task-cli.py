#!/usr/bin/env python3

import sys
import json
import os
from datetime import datetime


# Read the tasks.json file and stores it as list. 
# If the tasks.json file is not existing or isn't readable, create a empty list.
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as infile:
        try:
            tasks = json.load(infile)
        except json.JSONDecodeError:
            tasks = []
else:
    tasks = []


# Write the contents of tasks[] formatted in the tasks.json file.
# If file doesn't exist, create one.
def writeFile():
    try:
        with open("tasks.json", "w") as outfile:
            json.dump(tasks, outfile,  indent=2, sort_keys=False)
    except (IOError, OSError) as e:
        return 1
    except TypeError as e:
        return 2
    

# Add a new task
def add():
    new_task = {
            "id": 0,
            "description": sys.argv[2],
            "status": "todo",
            "createdAt": str(datetime.now()),
            "updatedAt": "not updated yet"
            }

    new_task["id"] = 0 if len(tasks) == 0 else tasks[len(tasks)-1]["id"]+1
    tasks.append(new_task)
    e = writeFile()
    
    if e == 1:
        print(f"Error writing to file: {e}")
    elif e == 2:
        print(f"Error serializing data: {e}")
    else:
        print("Task added successfully (ID: {})".format(new_task["id"]))


# Changes the description of the task in tasks.json
def update():
    for item in tasks:
        if item["id"] == int(sys.argv[2]):
            item["description"] = sys.argv[3]
            item["updatedAt"] = str(datetime.now())

    writeFile()


# Removes the task from tasks.json
def delete():
    for item in tasks:
        if item["id"] == int(sys.argv[2]):
            tasks.remove(item)

    writeFile()


# Changes the status of the task from tasks.json into in-progress
def markInProgress():
    for item in tasks:
        if item["id"] == int(sys.argv[2]):
            item["status"] = "in-progress"
            item["updatedAt"] = str(datetime.now())

    writeFile()


# Changes the status of the task from tasks.json into done
def markDone():
    for item in tasks:
        if item["id"] == int(sys.argv[2]):
            item["status"] = "done"
            item["updatedAt"] = str(datetime.now())

    writeFile()


# Prints every task in tasks.json with the status
def listTasks():
        if len(sys.argv) > 2:
            for item in tasks:
                if item["status"] == sys.argv[2]:
                    print(" id: {0}\n description: {1}\n status: {2}\n createdAt: {3}\n updatedAt: {4}\n".format(item["id"], item["description"], item["status"], item["createdAt"], item["updatedAt"]))
                    print("\n")
        else:
            for item in tasks:
                print(" id: {0}\n description: {1}\n status: {2}\n createdAt: {3}\n updatedAt: {4}\n".format(item["id"], item["description"], item["status"], item["createdAt"], item["updatedAt"]))



if __name__ == "__main__":
    user_input = sys.argv[1]

    match user_input:
        case "add":
            add()
        case "update":
            update()
        case "delete":
            delete()
        case "mark-in-progress":
            markInProgress()    
        case "mark-done":
            markDone()
        case "list":
            listTasks()
