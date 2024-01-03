#!/usr/bin/python3
"""
Script to gather data from a REST API for all employees
and export TODO list progress in JSON format.
"""

import json
from sys import argv
import requests


def get_all_employees_todo_progress():
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all user data
    users_response = requests.get(f"{base_url}users")
    users_data = users_response.json()

    # Create a dictionary to store tasks for all employees
    all_employees_tasks = {}

    for user_data in users_data:
        # Fetch TODO list data for each employee
        todo_response = requests.get(f"{base_url}todos?userId={user_data['id']}")
        todo_data = todo_response.json()

        # Store tasks in the dictionary
        user_tasks = [
            {
                "username": user_data['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todo_data
        ]

        all_employees_tasks[str(user_data['id'])] = user_tasks

    # Create JSON file
    json_file_path = "todo_all_employees.json"
    with open(json_file_path, 'w') as jsonfile:
        json.dump(all_employees_tasks, jsonfile)

    print(f"Data exported to {json_file_path}")


if __name__ == "__main__":
    get_all_employees_todo_progress()
