#!/usr/bin/python3
"""Script to gather data from a REST API for a given employee ID
and export TODO list progress in CSV format.
"""

import csv
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

    # Create CSV file
    csv_file_path = f"{employee_id}.csv"
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Write tasks to CSV
        for task in todo_data:
            writer.writerow({
                "USER_ID": user_data['id'],
                "USERNAME": user_data['username'],
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

    print(f"Data exported to {csv_file_path}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")

