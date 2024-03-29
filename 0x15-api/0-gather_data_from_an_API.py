#!/usr/bin/python3
"""This module fetches a data for a given employee id."""
import requests
import sys


if __name__ == "__main__":
    """this program fetches a data for a given employee id."""
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}".format(
                sys.argv[1])).json()
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                sys.argv[1])).json()
    name = user[0].get('name')
    taskDone = 0
    total = 0
    for todo in todos:
        total += 1
        if todo.get('completed') is True:
            taskDone += 1
    print(
            "Employee {} is done with tasks({}/{}):".format(
                name, taskDone, total))
    for todo in todos:
        if todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
