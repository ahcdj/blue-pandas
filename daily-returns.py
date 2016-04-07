"""Compute daily returns"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from util import get_data, get_data_offline, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def histogram():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data_offline(symbols, dates)
    # plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Plot a histogram
    daily_returns.hist(bins=20)

    # Calculate mean & standard deviation
    mean = daily_returns['SPY'].mean()
    std = daily_returns['SPY'].std()
    print "mean=", mean
    print "std=", std

    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std,color='r',linestyle='dashed',linewidth=2)

    plt.show()

    # Compute kurtosis
    print daily_returns.kurtosis()


def scatterplot():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY','XOM','GLD']
    df = get_data_offline(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter',x='SPY',y='XOM')
    beta_XOM,alpha_XOM = np.polyfit(daily_returns['SPY'],daily_returns['XOM'],1)
    print "beta_XOM= ", beta_XOM
    print "alpha_XOM= ", alpha_XOM
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
    plt.show()

    # Scatterplot SPY vs GLD
    daily_returns.plot(kind='scatter',x='SPY',y='GLD')
    beta_GLD,alpha_GLD = np.polyfit(daily_returns['SPY'],daily_returns['GLD'],1)
    print "beta_GLD= ", beta_GLD
    print "alpha_GLD= ", alpha_GLD
    plt.plot(daily_returns['SPY'], beta_GLD*daily_returns['SPY'] + alpha_GLD, '-', color='r')
    plt.show()

    # Calculate correlation coefficient
    print daily_returns.corr(method='pearson')

if __name__ == "__main__":
    # histogram()
    scatterplot()
