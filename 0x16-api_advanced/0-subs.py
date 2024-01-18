#!/usr/bin/python3
"""
a function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent':'CustomUserAgent'}
    url = f'https://www.redit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            subreddit_info = response.json().get('data', {})
            subscribers_count = subreddit_info.get('subscribers', 0)
            return f"OK {subscribers_count}"

        elif response.status_code == 404:
            return "Error"
        else: 
            print(f"Error: {response.status_code} - {response.text}")
            return "Error"

    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return "Error"
