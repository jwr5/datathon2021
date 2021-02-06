from reddit_parser import *
from analysis.vader import *
from parse import *
from sentiment import *
from visual import *
from subreddits import SUBS

POST_LIMIT = 200
COMMENT_LIMIT = 10


def main():
    master_list = []
    i = 1
    for subreddit in SUBS:
        print(i)
        i += 1
        master_list.extend(get_posts(subreddit, POST_LIMIT))
        print("Got posts")
        master_list.extend(get_comments(subreddit, POST_LIMIT, COMMENT_LIMIT))
        print("Got comments")

    print("5")
    companies = pruner_bigboy()
    print("6")
    sentiment_data, count_data, aver_data = get_company_sentiment(companies, master_list)
    top_sent_data = sort_data(sentiment_data)
    print("Sorted sentiment data")
    top_count_data = sort_data(count_data)
    print("Sorted count data")
    top_aver_data = sort_data(aver_data)
    print("Sorted average data")
    print("Finished")
    dict_to_graph(top_sent_data) 
    dict_to_graph(top_count_data) 
    dict_to_graph(top_aver_data)


main()
