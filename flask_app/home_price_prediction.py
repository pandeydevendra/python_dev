import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle
BASE_PATH = "/home/vins/Workspace/Py/python"
FILE_PATH_CSV = f"{BASE_PATH}/data_files/home_price/data.csv"
FILE_PATH_PICKLE = f"{BASE_PATH}/data_files/home_price/trained_model.pickle"

def predict_home_price(area):
    """
    load trained modal
    pass area and predict price
    @param area:
    @return: price
    """
    print(f"area: {area}")

    pass