import numpy as np
import pandas as pd

def parse_tickers_names(filename):
    df = pd.read_csv(filename, delimiter=',')
    exchange_list = df[['Symbol', 'Name']]
    return exchange_list

def df_concat(filenames):
    amex = parse_tickers_names('amex.csv')
    nyse = parse_tickers_names('nyse.csv')
    nasdaq = parse_tickers_names('nasdaq.csv')
    ticks_and_names = pd.concat([amex, nyse, nasdaq])
    return ticks_and_names

def df_cols_to_list(filenames):
    ticks_and_names = df_concat(filenames)
    ticks = ticks_and_names['Symbol'].tolist()
    companies = ticks_and_names['Name'].tolist()
    return ticks, companies

ticks, companies = df_cols_to_list(['amex.csv', 'nyse.csv', 'nasdaq.csv'])
print(ticks)
print(companies)