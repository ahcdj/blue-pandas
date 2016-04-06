"""
    AzureML Python client library wrapper
    Reference: https://github.com/Azure/Azure-MachineLearning-ClientLibrary-Python
"""

import os
import pandas as pd
from azureml import Workspace, AzureMLConflictHttpError
from azureml.serialization import DataTypeIds

ws = Workspace(workspace_id='a960dea614c04cf4a758c6321b857eb8', authorization_token='f527e8b37a58455494c08be5831119aa', endpoint='https://europewest.studio.azureml.net/')

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def read_ds(symbol):
    ds = ws.datasets[symbol_to_path(symbol, base_dir='')]
    df_temp = ds.to_dataframe()
    df_temp=df_temp.loc[:,['Date','Adj Close']].rename(columns={'Adj Close':symbol})
    df_temp.set_index('Date', inplace=True)
    df_temp.fillna('nan')
    return df_temp

def upload_df(filepath):
    filename = os.path.basename(filepath)
    print 'Uploading: ' + filename
    df_temp=pd.read_csv(filepath)
    # print df_temp.head()
    try:
        dataset = ws.datasets.add_from_dataframe(
            dataframe=df_temp,
            data_type_id=DataTypeIds.GenericCSV,
            name=filename,
            description=filename
        )
    except AzureMLConflictHttpError:
        print('Try again with a unique name!')
