#!/usr/bin/python3
"""This module makes a request to the reddits api."""
import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """returns a list containing all the hot posts in the subreddit."""
    payload = {"after": after}
    res = requests.get(
            "https://www.reddit.com/r/{}/hot/.json".format(
                subreddit), allow_redirects=False, headers={
                    "User-Agent": "Mozilla/5.0"}, params=payload)
    if res.status_code != 200:
        return None
    if len(word_count) == 0:
        for word in word_list:
            word_count[word.lower()] = 0
    res = res.json()
    for post in res.get('data').get('children'):
        title = post.get('data').get('title')
        for title_word in title.split():
            if title_word.lower() in word_count.keys():
                word_count[title_word.lower()] += 1

    after = res.get('data').get('after')
    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count != 0:
                print("{}: {}".format(word, count))
