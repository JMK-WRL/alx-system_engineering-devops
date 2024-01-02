#!/usr/bin/python3
"""
Script to gather data from a REST API for a given employee ID
and export TODO list progress in JSON format.
"""

import json
from sys import argv
import requests


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user_data = user_response.json()

    # Fetch TODO list data
    todo_response = requests.get(f"{base_url}todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Create JSON file
    json_file_path = f"{employee_id}.json"
    with open(json_file_path, 'w') as jsonfile:
        user_tasks = {
            str(user_data['id']): [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user_data['username']
                }
                for task in todo_data
            ]
        }
        json.dump(user_tasks, jsonfile)

    print(f"Data exported to {json_file_path}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
