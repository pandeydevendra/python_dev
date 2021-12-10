import pandas as pd

df = pd.read_csv("weather.csv")
print(df)

# melt process:

melted = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
print(melted)

# group once again:;

df_group = df.groupby("day")
print(df_group)

for city, data in df_group:
    print("city:",city, data)
    # print("\n")
    # print("data:",data)

for city, data in df_group:
    print("city:",city)
    print("\n")
    print("data:",data)