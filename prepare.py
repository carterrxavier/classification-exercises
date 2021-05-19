import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def prep_iris(df):
    df = df.drop_duplicates()
    cols_to_drop = ['Unnamed: 0','species_id']
    df = df.drop(columns=cols_to_drop)
    df = df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False,drop_first=True)
    df = pd.concat([df,dummy_df], axis=1)
    return df
    

def train_validate_test_split(df, target, seed = 450):
    train_validate, test = train_test_split(df, test_size = 0.2, 
                                            random_state = seed,
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size = 0.3,
                                       random_state = seed,
                                       stratify=train_validate[target])
    return train, validate, test
    