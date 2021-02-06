from reddit_parser import *
from analysis.vader import *
from parse import *
from sentiment import *
from visual import *


def main():
    POST_LIMIT = 750
    COMMENT_LIMIT = 50

    master_list = []
    print("starting")
    post_wall = get_posts('wallstreetbets', POST_LIMIT)
    post_stocks = get_posts('stocks', POST_LIMIT)
    post_inv = get_posts('investing', POST_LIMIT)
    post_penny = get_posts('pennystocks', POST_LIMIT)
    print("2")
    comment_wall = get_comments('wallstreetsbets', POST_LIMIT, COMMENT_LIMIT)
    comment_stocks = get_comments('stocks', POST_LIMIT, COMMENT_LIMIT)
    comment_inv = get_comments('investing', POST_LIMIT, COMMENT_LIMIT)
    comment_penny = get_comments('pennystocks', POST_LIMIT, COMMENT_LIMIT)
    print("three")
    master_list.extend(post_wall)
    master_list.extend(post_stocks)
    master_list.extend(post_inv)
    master_list.extend(post_penny)
    print("IV")
    master_list.extend(comment_wall)
    master_list.extend(comment_stocks)
    master_list.extend(comment_inv)
    master_list.extend(comment_penny)

    print("5")
    companies = pruner_bigboy()
    print("6")
    data = get_company_sentiment(companies, master_list)
    print("7")
    dict_to_graph(data)


main()
