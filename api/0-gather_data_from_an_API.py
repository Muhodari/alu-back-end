#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys

def get_employee_todo_progress(user_id):
    """ employees to todo progress """
    try:
        # Fetch employee information
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch tasks for the user
        task_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        task_response.raise_for_status()
        todos_data = task_response.json()

        # count number of completed tasks
        total_tasks = len(todos_data)
        done_tasks = [todo['title'] for todo in todos_data if todo['completed']]
        number_of_done_tasks = len(done_tasks)

        # Print the TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Invalid data received: missing key {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
