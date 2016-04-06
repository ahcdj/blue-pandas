"""Bulk upload CSV files to Azure Machine Learning Datasets"""

import os, glob
import pandas as pd
from azuremlds import upload_df

path = '/Users/hoonio/workspace/plutus/data'

def upload_csv():
    for csvfile in glob.glob(os.path.join(path, '*.csv')):
        upload_df(csvfile)

if __name__ == "__main__":
    upload_csv()
