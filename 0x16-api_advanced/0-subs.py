#!/usr/bin/python3
"""This module makes a request to the reddits api."""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers in the subreddit."""
    req = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(
                subreddit), allow_redirects=False)
    if req.status_code >= 300:
        return 0
    return req.json().get('data').get('subscribers')
