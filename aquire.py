import numpy as np
import pandas as pd
from env import host, user ,password
from pydataset import data
import os

def get_connection(db, user = user, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def new_titanic_data():
    file_name = 'titanic.csv'
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    
    else:
        query = ''' select * from passengers'''   
        df = pd.read_sql(query,get_connection('titanic_db'))
        df.to_csv(file_name)
        return df



def new_iris_data():
    file_name = 'iris.csv'
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    else:
        query = '''SELECT  species.species_id, species_name ,sepal_length,sepal_width,  petal_length,petal_width
                FROM measurements
                JOIN species on measurements.species_id = species.species_id
             '''
        df = pd.read_sql(query,get_connection('iris_db'))
        df.to_csv(file_name)
        return df