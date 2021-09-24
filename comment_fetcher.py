import json
import pandas as pd
import requests
import comment_generator
import config
import time

"Main gets posts which have the url below in them: " \
"https://www.reddit.com/r/investing/comments/prw7it/chinas_growing_property_crisis_a_look_onto_a_few.json " \
"Aim here is to return df with comments for each post"

def get_reddit_comments(url):
    try:
        base_url = f'{url}.json'
        request = requests.get(base_url, headers={'User-agent': 'yourbot'})
    except:
        print('An Error Occurred')
    return request.json()

def get_post_comments(commenturl):
    comments = []
    for comment in comments['data']['children']:
        x = comment['data']['comment']
        comments.append(x)
    return comments

def get_comments(r):
    '''
        Create a DataFrame with comments.
    '''
