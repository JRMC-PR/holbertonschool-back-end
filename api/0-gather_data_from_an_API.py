#!/usr/bin/python3
"""
This module uses Python to make requests to a REST API.
fix
It fetches data about a specific employee's tasks
and prints a summary of the tasks completed and the
titles of the completed tasks.
"""
import requests
import sys


# Get the employee ID from the command line arguments
employee_id = sys.argv[1]

# Send a GET request to the API to get the user data
user_response = requests.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)

# Parse the response data as JSON
data = user_response.json()

# Extract the employee's name from the data
employee_name = data['name']

# Send another GET request to the API to get the todo data
todos_response = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

# Parse the todo data as JSON
todos_data = todos_response.json()

# Calculate the total number of tasks
total_todos = str(len(todos_data))

# Calculate the number of completed tasks
completed_todos = str(sum(1 for task in todos_data if task['completed']))

# Print the first line of the output
print("Employee " + employee_name + " is done with tasks(" +
      completed_todos + "/" + total_todos + "):")

# Print the title of each completed task
for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])

if __name__ == '__main__':
    pass
