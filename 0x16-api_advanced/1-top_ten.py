#!/usr/bin/python3
"""This module makes a request to the reddits api."""
import requests


def top_ten(subreddit):
    """prints the top 10 posts in the subreddit"""
    res = requests.get(
            "https://www.reddit.com/r/{}/hot/.json".format(
                subreddit), allow_redirects=False, headers={
                    "User-Agent": "Mozilla/5.0"})
    if res.status_code != 200:
        print("None")
        return
    res = res.json()
    i = 0
    for post in res.get('data').get('children'):
        if i == 10:
            break
        print(post.get('data').get('title'))
        i += 1
