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
                  'ANY', 'SUN', 'TD', 'FUND', 'NOW', 'NEXT', 'TV', 'NOW', 'ONE', 
                  'TM', 'PM', 'PT', 'AI', 'CBD','UK','USA','CRY','SELF','GS', 'LIFE'
                  'TREE', 'GROW'])


def similar(a, b, min_similarity=SIMILARITY_THRESHOLD):
    return SequenceMatcher(None, a, b).ratio() > min_similarity


def get_company_sentiment(company_names, comments):
    sentiment_data = dict()
    count_data = dict()

    for comment in comments:
        sent_score = sentiment_score(comment)
        val = sent_score[1]
        for ticker, company in company_names:
            if (comment.find(" " + ticker + " ") >= 0 or comment.find(" $" + ticker + " ") >= 0) and ticker not in black_list:
                if not ticker in sentiment_data:
                    sentiment_data[ticker] = val
                    count_data[ticker] = 1
                else:
                    sentiment_data[ticker] += val
                    count_data[ticker] += 1
    aver_data = {key: (sentiment_data[key])/count_data[key] for key in sentiment_data.keys()}
    sentiment_lst = [(ticker, val) for ticker, val in sentiment_data.items()]
    count_lst = [(ticker, val) for ticker, val in count_data.items()]
    aver_lst = [(ticker, val) for ticker, val in aver_data.items()]
    sort_sent = sorted(sentiment_lst, key=lambda x: x[1])
    sort_count = sorted(count_lst, key=lambda x: x[1])
    sort_aver = sorted(aver_lst, key=lambda x: x[1])
    print(sort_sent, sort_count, sort_aver)
    return sort_sent, sort_count, sort_aver



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

def sort_data(lst):
    if len(lst) < 20:
        return {key: val for key, val in lst}
    top_values = lst[:10] + lst[-10:]
    return {key: val for key, val in top_values}
