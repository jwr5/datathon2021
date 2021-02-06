import numpy as np
import pandas as pd

def parse_tickers_names(filename):
    df = pd.read_csv(filename, delimiter=',')
    exchange_list = df[['Symbol', 'Name']]
    return exchange_list

def df_concat(filenames):
    ticks_and_names = parse_tickers_names(filenames[0])
    for exchange in filenames[1:-1]:
        exchange_temp = parse_tickers_names(exchange)
        ticks_and_names = pd.concat([ticks_and_names, exchange_temp])
    return ticks_and_names

def df_cols_to_list(filenames):
    ticks_and_names = df_concat(filenames)
    ticks = ticks_and_names['Symbol'].tolist()
    companies = ticks_and_names['Name'].tolist()
    return ticks, companies

ticks, companies = df_cols_to_list(['amex.csv', 'nyse.csv', 'nasdaq.csv'])
print(ticks)
print(companies)