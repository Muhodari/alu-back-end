#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import requests
from sys import argv


def get_employee_info(employee_id):
    """
    Get employee information by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_employee_todos(employee_id):
    """
    Get the TODO list of the employee by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_employee_todo_progress(employee_id):
    """
    Fetch and display employee's TODO list progress
    """
    try:
        employee = get_employee_info(employee_id)
        employee_name = employee.get("name")

        emp_todos = get_employee_todos(employee_id)
        tasks = {todo.get("title"): todo.get("completed")
                 for todo in emp_todos}

        total_tasks = len(tasks)
        completed_tasks = [
            title for title, completed in tasks.items() if completed]
        completed_tasks_count = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks"
              f"({completed_tasks_count}/{total_tasks}):")
        for title in completed_tasks:
            print(f"\t {title}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Invalid data received: missing key {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
