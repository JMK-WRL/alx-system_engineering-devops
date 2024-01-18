#!/usr/bin/python3
"""
Returns number of subscribers for a subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
  """
  Queries the Reddit API and returns the number of 
  subscribers for the given subreddit.
  
  Parameters:
    subreddit (str): The subreddit name
  
  Returns:
    int: Number of subscribers, or 0 if invalid subreddit
  """
  
  # Set custom User-Agent to avoid rate limiting
  headers = {'User-Agent': 'MyBot'} 
  
  # API endpoint for subreddit about page
  url = f'https://www.reddit.com/r/{subreddit}/about.json'
  
  try:
    # Make GET request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Raise exception for 4xx/5xx statuses
    response.raise_for_status()
    
  except requests.exceptions.HTTPError:
    # Return 0 for any HTTP errors
    return 0

  # Parse response as JSON
  data = response.json() 
  
  # Extract and return subscriber count 
  return data['data']['subscribers']
