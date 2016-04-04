"""Plot High prices for IBM"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from azureml import Workspace

ws = Workspace(workspace_id='a960dea614c04cf4a758c6321b857eb8', authorization_token='f527e8b37a58455494c08be5831119aa', endpoint='https://europewest.studio.azureml.net/')

def read_from_azureml(symbol):
    ds = ws.datasets[symbol_to_path(symbol, base_dir='')]
    df_temp = ds.to_dataframe()
    df_temp=df_temp.loc[:,['Date','Adj Close']].rename(columns={'Adj Close':symbol})
    df_temp.set_index('Date', inplace=True)
    df_temp.fillna('nan')
    return df_temp

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("{}.csv".format(symbol))  # read in data
    # TODO: Compute and return the mean volume for this stock
    return df['Volume'].mean()

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files """
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = read_from_azureml(symbol)
        # df_temp=pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        # df_temp=df_temp.rename(columns={'Adj Close':symbol})
        print(df_temp.head())
        df=df.join(df_temp,how='inner')
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
    # reverse to incrementing date order
    return df.iloc[::-1]

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
    #"""Function called by Test Run."""
    #for symbol in ['AAPL', 'IBM']:
        #print "Mean Volume"
        #print symbol, get_mean_volume(symbol)

    # df = pd.read_csv("data/IBM.csv")
    #print df.head(5)
    #return df['Volume'].mean()

    dates=pd.date_range('2010-01-01', '2010-12-31')
    symbols =['GOOG','IBM','GLD']

    df1 = get_data(symbols, dates)
    # print df1.ix['2010-03-01':'2010-04-01', ['SPY','IBM']]
    # print df1
    # plot_data(df1)
    plot_selected(df1, ['SPY', 'IBM', 'GOOG'], '2010-03-01', '2010-04-01')

if __name__ == "__main__":
    test_run()
