from azuremlds import read_ds
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def get_data(symbols, dates, join='inner'):
    """Read stock data (adjusted close) for given symbols from CSV files """
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = read_ds(symbol)
        df=df.join(df_temp,how=join)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    # reverse to incrementing date order
    return df.iloc[::-1]
