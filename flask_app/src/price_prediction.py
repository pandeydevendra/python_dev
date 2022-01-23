import pandas as pd
import numpy as np
from sklearn import linear_model
import sys
sys.path.append('../src')
import pickle
from src.constant import FILE_PATH_PICKLE


def load_trained_model():
    with open(FILE_PATH_PICKLE, 'rb') as f:
        p_model = pickle.load(f)
        return p_model


def price_by_area(area):
    """
    load trained modal
    pass area and predict price
    @param area:
    @return: price
    """
    print(f"area: {area}")
    # import ipdb; ipdb.set_trace();
    # return area
    trained_model = load_trained_model()
    area = int(area)
    h_price = trained_model.predict([[area]])
    # import ipdb; ipdb.set_trace();
    print(f"h_price:: {h_price}")
    return round(h_price[0])

#
# def predict_home_price(area, bed, age):
#     """
#
#     @param area:
#     @param bed:
#     @param age:
#     @return:
#     """
#     print(globals())

price_by_area()
