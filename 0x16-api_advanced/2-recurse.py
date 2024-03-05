#!/usr/bin/python3
"""This module makes a request to the reddits api."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing all the hot posts in the subreddit."""
    payload = {"after": after}
    res = requests.get(
            "https://www.reddit.com/r/{}/hot/.json".format(
                subreddit), allow_redirects=False, headers={
                    "User-Agent": "Mozilla/5.0"}, params=payload)
    if res.status_code != 200:
        return None
    res = res.json()
    for post in res.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))

    after = res.get('data').get('after')
    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
