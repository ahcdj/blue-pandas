"""Compute daily returns"""

import os
import pandas as pd
from util import get_data, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # daily_returns = df.copy()
    # daily_returns[1:] = (df[1:] / df[:-1].values) - 1

    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def daily_return():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')  # one month only
    symbols = ['SPY','XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

if __name__ == "__main__":
    daily_return()
