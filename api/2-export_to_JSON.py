#!/usr/bin/python3
"""
This module uses Python to make requests to a REST API.
q
It fetches data about a specific employee's tasks
and prints a summary of the tasks completed and the
titles of the completed tasks.
"""
import json
import requests
import sys


# Get the employee id
employee_id = sys.argv[1]
# Set the url and get a respnse
user_response = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{employee_id}')
# Get data in json form

data = user_response.json()
# Get the name of the employee
employee_name = data['name']

# Get the todo data fro the API
todos_response = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
# Get the data in json form
todos_data = todos_response.json()

# Get the total number of tasks
total_todos = len(todos_data)
# Get the number of completed tasks
ok_todos = sum(1 for task in todos_data if task['completed'])

# Print the first line of the output
print(
    f'Employee {employee_name} is done with tasks({ok_todos}/{total_todos}):')

# Print the title of each completed task
for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])

# Export using JSON Format
with open('USER_ID.json', 'w') as jsonfile:
    json.dump({employee_id: [{
        "task": task['title'],
        "completed": task['completed'],
        "username": employee_name
    } for task in todos_data]}, jsonfile)

if __name__ == '__main__':
    pass
