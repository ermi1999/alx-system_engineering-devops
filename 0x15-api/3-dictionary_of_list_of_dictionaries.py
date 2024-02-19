#!/usr/bin/python3
"""This module fetches a data for a given employee id."""
import json
import requests
import sys


if __name__ == "__main__":
    """this program fetches a data for a given employee id."""
    users = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()
    _dict = {}
    for user in users:
        name = user.get('name')
        userId = user.get('id')
        _dict[userId] = []
        todos = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                    userId)).json()
        for todo in todos:
            data = {"task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user.get('username')}
            _dict.get(userId).append(data)
    with open("todo_all_employees.json", 'w') as f:
        f.write(json.dumps(_dict))
