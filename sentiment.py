from analysis.vader import sentiment_score

from difflib import SequenceMatcher

SIMILARITY_THRESHOLD = 0.65

black_list = set(['A', 'GO', 'DD', 'RH', 'TO', 'HOLD', 'UP',
                  'THE', 'CAN', 'STAY', 'SO', 'K', 'L', 'OUT',
                  'BY', 'BUY', 'DM', 'COST', 'PAYS', 'AM', 'RUN',
                  'IS', 'THE', 'ELSE', 'ARE', 'HOME', 'ARE', 'BIG', 'EAT',
                  'YOLO', 'PUMP', 'EOD', 'IPO', 'ATH', 'B', 'C', 'D', 'E',
                  'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'RC', 'SEE', 'AN',
                  'FOR', 'IQ', 'ALL', 'CEO', 'OR', 'NET', 'SHO', 'ON', 'VERY', 'AT',
                  'IT', 'LOW', 'REAL', 'TRUE', 'SU', 'SI', 'SAFE', 'BE', 'HUGE',
                  'NEW', 'HEAR', 'JP', 'HOPE', 'TELL', 'BEST', 'LOVE', 'IP', 'FCF',
                  'ANY', 'SUN', 'TD', 'FUND', 'NOW', 'NEXT', 'TV', 'NOW', 'ONE', 'TM', 'PM', 'PT', 'AI', 'CBD'])


def similar(a, b, min_similarity=SIMILARITY_THRESHOLD):
    return SequenceMatcher(None, a, b).ratio() > min_similarity


def get_company_sentiment(company_names, comments):
    # company_names - [(ticker, company_name)]
    # comments - ['comment1', 'comment2']
    sentiment_data = dict()

    for comment in comments:
        sent_score = sentiment_score(comment)
        val = sent_score[1]
        for ticker, company in company_names:
            if (comment.find(" " + ticker + " ") >= 0 or comment.find(" $" + ticker + " ") >= 0) and ticker not in black_list:
                if not ticker in sentiment_data:
                    sentiment_data[ticker] = val
                else:
                    sentiment_data[ticker] += val
    lst = [(ticker, val) for ticker, val in sentiment_data.items()]
    sorted_lst = sorted(lst, key=lambda x: x[1])
    if len(sorted_lst) < 20:
        return {key: val for key, val in sorted_lst}
    top_values = sorted_lst[:10] + sorted_lst[-10:]
    return {key: val for key, val in top_values}



def get_company_count(company_names, comments):
    count_data = dict()
    for comment in comments:
        for ticker, company in company_names:
            if (comment.find(" " + ticker + " ") >= 0 or comment.find(" $" + ticker + " ") >= 0) and ticker not in black_list:
                if not ticker in count_data:
                    count_data[ticker] = 1
                else:
                    count_data[ticker] += 1
                    
    lst = [(ticker, val) for ticker, val in count_data.items()]
    sorted_lst = sorted(lst, key=lambda x: x[1])

    if len(sorted_lst) < 20:
        return {key: val for key, val in sorted_lst}

    top_values = sorted_lst[:20]
    return {key: val for key, val in top_values}

    
