import requests
from subreddits import SUBS
import requests.auth
from credentials import CLIENT_ID, CLIENT_SECRET
import praw
import pandas as pd

#Helper function. Returns an instance of the Reddit class
def get_reddit():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": "rice_stock_analysis", "password": "ricedatathon2021"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by rice_stock_analysis"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    response.json()
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                    user_agent="android:com.example.myredditapp:v1.2.3 (by u/rice_stock_analysis)")
    return reddit


#returns a list of strings from the comments
def get_comments(sub, post_limit, comment_limit):
    
    reddit = get_reddit()
    subreddit = reddit.subreddit(sub)
    hot_sub = subreddit.hot(limit = post_limit)
    master_list = []
    
    for submission in hot_sub:
        comments = submission.comments
        limit = 0
        for comment in comments:
            if limit > comment_limit:
                break
            master_list.append(comment.body)
            limit = limit + 1
    return master_list

#returns a list of strings from the bodies of posts
def get_posts(sub, post_limit):
    
    reddit = get_reddit()
    subreddit = reddit.subreddit(sub)
    hot_sub = subreddit.hot(limit = post_limit)
    master_list = []
    
    for submission in hot_sub:
        master_list.append(submission.selftext)
    
    return master_list


#returns a list of strings from the titles of posts
def get_titles(sub, post_limit):
    
    reddit = get_reddit()
    subreddit = reddit.subreddit(sub)
    hot_sub = subreddit.hot(limit = post_limit)
    master_list = []
    

    for submission in hot_sub:
        master_list.append(submission.title)
    
    return master_list
