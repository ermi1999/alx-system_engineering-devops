#!/usr/bin/python3
"""This module fetches a data for a given employee id."""
import json
import requests
import sys


if __name__ == "__main__":
    """this program fetches a data for a given employee id."""
    userId = sys.argv[1]
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}".format(
                userId)).json()
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                userId)).json()
    name = user[0].get('name')
    _dict = {userId: []}
    for todo in todos:
        data = {"task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user[0].get('username')}
        _dict.get(userId).append(data)
    with open("{}.json".format(userId), 'w') as f:
        f.write(json.dumps(_dict))
