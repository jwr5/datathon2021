from reddit_parser import *

data = get_posts_extra('wallstreetbets', 20)


def score(posts):
    return sorted(posts, key=lambda student: student[1] + 100 * student[2])


print(score(data))
