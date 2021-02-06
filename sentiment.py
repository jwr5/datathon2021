from analysis.vader import sentiment_score

from difflib import SequenceMatcher

SIMILARITY_THRESHOLD = 0.65


def similar(a, b, min_similarity=SIMILARITY_THRESHOLD):
    return SequenceMatcher(None, a, b).ratio() > min_similarity

# Iterate through each word in a comment
# Compare if two strings are similar enough to be considered the same
# if they are, calculate the sentiment score of the comment associated with the
# matched string


def get_company_sentiment(company_names, comments):
    # company_names - [(ticker, company_name)]
    # comments - ['comment1', 'comment2']
    sentiment_data = dict()
    for comment in comments:
        lower_comment = comment.lower()
        for word in lower_comment.split():
            for ticker, company in company_names:
                if similar(word, ticker) or similar(word, company):
                    if not company in sentiment_data:
                        sentiment_data[ticker] = sentiment_score(comment)[1]
                    else:
                        sentiment_data[ticker] += sentiment_score(comment)[1]
    return sentiment_data
