"""
in loop
continue/stop
ask required input
predict target value
keep on ...
"""
# import all required modelus

import pickle
from constant import FILE_PATH_PICKLE


def load_trained_pickle_model():
    """
    load the pickle model (already trained and saved model as pickle file);
    @return: pickle model
    """
    with open(FILE_PATH_PICKLE, 'rb') as f:
        pkl_model = pickle.load(f)
        return pkl_model


def predict_home_price(n):
    """
    using already trained, loaded, pickle model predict target value (home-price)
    @param n: number of bedrooms
    @return: predicted price as a model
    """
    saved_trained_model = load_trained_pickle_model()
    predicted_price = saved_trained_model.predict([[n]])
    return predicted_price


keep_on = True
while keep_on is True:
    choice = input("Do you want to predict home-price? y/n: ")
    if choice == 'y':
        beds = int(input("Enter the number of bedrooms to calculate the home-price: "))
        home_price = predict_home_price(beds)
        print(f"The price of home with {beds} bedrooms is {home_price}")
    elif choice == 'n':
        keep_on = False
        print("Thank you for using the prediction program. \nEoP!!!")
    else:
        print("Kindly enter correct choice. \nTry again!!!\n")
