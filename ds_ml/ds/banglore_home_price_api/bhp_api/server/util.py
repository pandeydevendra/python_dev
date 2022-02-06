import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath, balcony):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]
        # first 4 columns are [{"total_sqft"(0), "bath"(1),"balcony"(2),"bhk"(3)},"1st block hrbr layout"(4)

    global __model
    if __model is None:
        with open('./artifacts/bhp_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(f"The Estimated Price = {get_estimated_price('1st Phase JP Nagar', 1000, 3, 3, 2)} lakhs")
    print(f"The Estimated Price = {get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 2)} lakhs")
    print(f"The Estimated Price = {get_estimated_price('Kalhalli', 1000, 2, 2, 1)} lakhs")  # other location
    print(f"The Estimated Price = {get_estimated_price('Ejipura', 1000, 2, 2, 1)} lakhs")  # other location
