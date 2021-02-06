from reddit_parser import *
from analysis.vader import *

data = get_posts_extra('wallstreetbets', 20)
scored_data = sentiment_scores(data)
positive_data = []
negative_data = []


def find_important_positive_posts(posts):
    for post in posts:
        if post[3] > 0.2:
            positive_data.append(post)
    return sorted(positive_data, key=lambda post: post[1] + 100 * post[2])


def find_important_negative_posts(posts):
    for post in posts:
        if post[3] < 0.2:
            negative_data.append(post)
    return sorted(negative_data, key=lambda post: post[1] + 100 * post[2])
