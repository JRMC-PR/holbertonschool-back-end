#!/usr/bin/python3
"""
This module uses Python to make requests to a REST API. It fetches data about a specific employee's tasks
and prints a summary of the tasks completed and the titles of the completed tasks.
"""
import requests
import json


# Reuet data for users
users = requests.get('https://jsonplaceholder.typicode.com/users').json()

# make an empty dictionary
all_tasks = {}

# Loop over all users
for user in users:
    # get the user id and name
    user_id = user['id']
    user_name = user['username']

    # get the list
    todo_list = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

    # format the task as indicated
    task_list = [{'username': user_name, 'task': task.get(
        'title'), 'completed': task.get('completed')} for task in todo_list]

    # Adds the task to the dictionary
    all_tasks[user_id] = task_list

# Export using Json format
with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(all_tasks, jsonfile)
