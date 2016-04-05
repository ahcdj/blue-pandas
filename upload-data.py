"""
    Bulk upload CSV files to Azure Machine Learning Datasets
    Library reference: https://github.com/Azure/Azure-MachineLearning-ClientLibrary-Python
"""

import os, glob
import pandas as pd
from azureml import Workspace, AzureMLConflictHttpError
from azureml.serialization import DataTypeIds

ws = Workspace(workspace_id='a960dea614c04cf4a758c6321b857eb8', authorization_token='f527e8b37a58455494c08be5831119aa', endpoint='https://europewest.studio.azureml.net/')
path = '/Users/hoonio/workspace/python/ud120-projects/ml4t/data'
# path = '/Users/hoonio/workspace/plutus/data'

def upload_csv():
    for csvfile in glob.glob(os.path.join(path, '*.csv')):
        filename = os.path.basename(csvfile)
        print 'Uploading: ' + filename
        df_temp=pd.read_csv(csvfile)
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


if __name__ == "__main__":
    upload_csv()
