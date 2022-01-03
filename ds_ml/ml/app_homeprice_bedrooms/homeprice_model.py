"""
homeprice based on number of bedrooms

RoadMap >> <1>Create-DataFrame > <2>Train-Model > <3>Save-pickle

"""
import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle

from constant import FILE_PATH_CSV, FILE_PATH_PICKLE


def create_homeprice_dataframe():
    """
    @return: DataFrame
    """
    h_df = pd.read_csv(FILE_PATH_CSV)
    h_df.bedrooms = h_df.fillna(h_df.bedrooms.mean())
    # print(df) # checked df >> ok
    return h_df


# print(create_homprice_dataframe())  # used while checking df <<>>

def train_homeprice_model():
    """
    DataFrame needed to train model >> h_df being called from upper function
    @return: train model
    """
    df = create_homeprice_dataframe()
    h_model = linear_model.LinearRegression()
    h_model.fit(df[['bedrooms']], df.price)
    return h_model


# print(train_homeprice_model())  # used while checking h_mode ;;

# Finally save this trained model >> into >> a pickle file

def save_as_p_model(model):
    with open(FILE_PATH_PICKLE, 'wb') as f:
        pickle.dump(model, f)


trained_model = train_homeprice_model()
save_as_p_model(trained_model)
# run only once to avoid creating multiple pickle files in the background
