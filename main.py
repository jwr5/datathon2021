from reddit_parser import *
from analysis.vader import *
from parse import *
from sentiment import *
from visual import *
from subreddits import SUBS

POST_LIMIT = 750
COMMENT_LIMIT = 50


def main():
    master_list = []
    i = 1
    for subreddit in SUBS:
        print(i)
        i += 1
        master_list.extend(get_posts(subreddit, POST_LIMIT))
        master_list.extend(get_comments(subreddit, POST_LIMIT, COMMENT_LIMIT))

    print("5")
    companies = pruner_bigboy()
    print("6")
    data = get_company_count(companies, master_list)
    print("7")
    dict_to_graph(data)


main()
