import pandas as pd

df = pd.read_excel("/home/vins/Workspace/Py/python/ds_ml/pandas/wa_weather_1944_till_2016.xlsx", engine='openpyxl')

# print(df)

weather_data = {
    'day': ['01/01/2017', '01/02/2017', '01/03/2017'],
    'temperature': [32, 35, 28],
    'windspeed': [6, 7, 4],
    'event': ['Rain', 'Sunny', 'Snow']
}

# print(weather_data)

df_dict = pd.DataFrame(weather_data)

# print(df_dict)

weather_data_tuple = [
    ('01/01/17', 32, 6, 'Rain'),
    ('01/02/17', 35, 7, 'Sunny'),
    ('01/03/17', 28, 2, 'Snow'),
]
df_tuple = pd.DataFrame(weather_data_tuple, columns=["day", "temperature", "windspeed", "event"])

# print(weather_data_tuple)`
# print(df_tuple)

weather_list_of_dict = [
    {'day': '1/1/2017', 'temperature': 36, 'windspeed': 8, 'event': 'sunny'},
    {'day': '2/1/2017', 'temperature': 32, 'windspeed': 10, 'event': 'cloudy'},
    {'day': '3/1/2017', 'temperature': 28, 'windspeed': 6, 'event': 'rain'},
    {'day': '4/1/2017', 'temperature': 26, 'windspeed': 2, 'event': 'snow'}
]

print(weather_list_of_dict)

df_list_dict = pd.DataFrame(weather_list_of_dict)

print(df_list_dict)
