"""
in loop
continue/stop
ask required input
predict
keep on ...
"""

# get a pickle model
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle
from constant import FILE_PATH_PICKLE


def load_trained_model():
    with open(FILE_PATH_PICKLE, 'rb') as f:
        p_model = pickle.load(f)
        return p_model


# use pickle model to predict home price

def predict_homeprice():
    trained_model = load_trained_model()
    area = float(input("Enter area of the home for home-price prediction: "))
    h_price = trained_model.predict([[area]])
    print(f"The of home of area {area} is {h_price}")


keep_on = True
while keep_on == True:
    choice = input("Do you want to predict home-price, y?n: ")
    if choice == 'y':
        predict_homeprice()
    elif choice == 'n':
        keep_on = False
        print("end of the program")
    else:
        print("Enter valid response.")
