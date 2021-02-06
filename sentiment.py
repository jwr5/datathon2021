from analysis.vader import sentiment_score


def get_company_sentiment(company_names, comments):
    # company_names - [(ticker, company_name)]
    # comments - ['comment1', 'comment2']
    sentiment_data = dict()
    for comment in comments:
        lower_comment = comment.lower()
        for ticker, company in company_names:
            if lower_comment.find(ticker.lower()) > 0 or lower_comment.find(company.lower()) > 0:
                if not company in sentiment_data:
                    sentiment_data[company] = sentiment_score(lower_comment)
                else:
                    sentiment_data[company] += sentiment_score(lower_comment)
    return sentiment_data
