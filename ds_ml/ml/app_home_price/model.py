"""
data set for homperice

"""
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle

from constant import FILE_PATH_CSV, FILE_PATH_PICKLE


def trained_p_model():
    # import ipdb; ipdb.set_trace();
    df = pd.read_csv(FILE_PATH_CSV)
    model = linear_model.LinearRegression()
    model.fit(df[['area']], df.price)
    print(model.coef_)
    print(model.intercept_)
    print(model.predict([[5000]]))
    return model


def save_p_model(model):
    with open(FILE_PATH_PICKLE, 'wb') as f:
        pickle.dump(model, f)


trained_model = trained_p_model()
save_p_model(trained_model)
