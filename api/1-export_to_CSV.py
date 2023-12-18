#!/usr/bin/python3
"""
This script fetches data from a REST API for a given employee ID, prints the employee's TODO list progress,
and exports the data to a CSV file.

Usage: python3 1-export_to-CSV.py [employee_id]

The CSV file will have the following format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import requests
import sys
import csv


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

# export using csv format
with open('USER_ID.csv', 'w') as csvfile:
    # creating a csv writer object
    # quoting=csv.QUOTE_ALL to quote all the fields
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in todos_data:
        # writing the fields to the csv file
        writer.writerow([employee_id, employee_name, task['completed'],
                         task['title']])
