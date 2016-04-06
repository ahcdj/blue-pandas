"""Plot High prices for IBM"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from util import get_data

def plot_data(df,title="Stock prices"):
    '''Plot stock prices'''
    ax = normalize_data(df).plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, selected_stocks, start_date, end_date):
    plot_data(df.ix[start_date:end_date, selected_stocks])

def normalize_data(df):
    '''Normalize stock prices using the first row of the dataframe'''
    return df/df.ix[0,:]

def test_run():
    dates=pd.date_range('2010-01-01', '2010-12-31')
    symbols =['GOOG','IBM','GLD']

    df1 = get_data(symbols, dates)
    # print df1.ix['2010-03-01':'2010-04-01', ['SPY','IBM']]
    # print df1
    # plot_data(df1)
    plot_selected(df1, ['SPY', 'IBM', 'GOOG'], '2010-03-01', '2010-04-01')

if __name__ == "__main__":
    test_run()
