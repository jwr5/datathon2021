import numpy as np
import pandas as pd
from collections import defaultdict

def parse_tickers_names(filename):
    df = pd.read_csv(filename, delimiter=',')
    exchange_list = df[['Symbol', 'Name']]
    return exchange_list

def df_concat(filenames):
    ticks_and_names = pd.DataFrame()
    for exchange in filenames:
        exchange_temp = parse_tickers_names(exchange)
        ticks_and_names = pd.concat([ticks_and_names, exchange_temp])
    return ticks_and_names

def df_cols_to_list(filenames):
    ticks_and_names = df_concat(filenames)
    ticks = ticks_and_names['Symbol'].tolist()
    companies = ticks_and_names['Name'].tolist()
    return ticks, companies

def company_pruner(company_list, cutoff_frequency):
    pruned_list = []
    cl_copy = company_list.copy()
    #split_list = [[item.split(' ')] for item in cl_copy]
    split_list = cl_copy
    word_freq = defaultdict(int)
    for company_name in split_list:
        for word in company_name:
            word = tuple(word)
            word_freq[word] += 1
    
    for word, freq in word_freq.items():
        for company_name in split_list:
            if word in company_name and (freq >= cutoff_frequency):
                company_name.remove(word)
    
    for company_name in split_list:
        comp_string = ' '.join([str(word) for word in company_name])
        pruned_list.append(comp_string)

    return pruned_list

def zip_list(list1, list2):
    zip_list = tuple(zip(list1, list2))
    return zip_list

ticks, companies = df_cols_to_list(['amex.csv', 'nyse.csv', 'nasdaq.csv'])
print(ticks)
print(companies)
pruned_lst = company_pruner(companies, 20)
print(pruned_lst)