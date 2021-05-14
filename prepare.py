import numpy as np
import pandas as pd


def prep_iris(df):
    df = df.drop_duplicates()
    cols_to_drop = ['Unnamed: 0','species_id']
    df = df.drop(columns=cols_to_drop)
    df = df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False)
    df = pd.concat([df,dummy_df], axis=1)
    return df
    