#!/usr/bin/python3
"""This module fetches a data for a given employee id."""
import csv
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
    username = user[0].get('username')
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                    [sys.argv[1], username,
                     str(todo.get('completed')),
                     todo.get('title')])
