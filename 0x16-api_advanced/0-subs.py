#!/usr/bin/python3
"""
A fuction that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    about_url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    response = requests.get(about_url, headers={'User-Agent': 'YourApp/1.0'})
    if response.status_code == 200:
        data = response.json()
        return int(data['data']['subscribers'])
    else:
        return 0
