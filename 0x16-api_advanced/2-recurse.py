#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The parameter used for pagination in Reddit API.

    Returns:
        list: A list containing the titles of all hot articles for the subreddit.
              If no results are found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list

        for post in posts:
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)

        after = data.get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

    return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
