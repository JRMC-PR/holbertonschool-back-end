#!/usr/bin/python3
"""
This module uses Python to make requests to a REST API.
It fetches data about a specific employee's tasks
and prints a summary of the tasks completed and the
titles of the completed tasks.
"""
import requests
import sys


# get the employee id
employee_id = sys.argv[1]
# set the url and get a respnse
user_response = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{employee_id}')
# get data in json form

data = user_response.json()
# get the name of the employee
employee_name = data['name']

# get the todo data fro the API
todos_response = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
# get the data in json form
todos_data = todos_response.json()

# get the total number of tasks
total_todos = len(todos_data)
# get the number of completed tasks
ok_todos = sum(1 for task in todos_data if task['completed'])

# Print the first line of the output
print(
    f'Employee {employee_name} is done with tasks({ok_todos}/{total_todos}):')

# Print the title of each completed task
for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])
