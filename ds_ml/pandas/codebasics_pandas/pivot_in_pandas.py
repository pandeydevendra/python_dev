import pandas as pd
import numpy as np

df = pd.read_csv("weather.csv")
print(df)

df_pivot = df.pivot(index='city', columns='date')
print(df_pivot)
df_pivot = df.pivot(index='date', columns='city')
print(df_pivot)

df1 = df.pivot(index='city', columns='date', values="humidity")
print(df1)

df1 = df.pivot(index='city', columns='date', values="temperature")
print(df1)

df2 = df.pivot(index='humidity', columns='city')
print(df2)

df = pd.read_csv("weather2.csv")
print(df)

df_pivot1 = df.pivot_table(index="city", columns="date")
print(df_pivot1)

df_pivot_margin = df.pivot_table(index="city", columns="date", margins=True, aggfunc=np.sum)
print(df_pivot_margin)
df_pivot_margin = df.pivot_table(index="date", columns="city", margins=True, aggfunc=np.sum)
print(df_pivot_margin)

df2 = pd.read_csv("weather3.csv")
print(df2)

df2['date'] = pd.to_datetime(df2['date'])
df_group = df2.pivot_table(index=pd.Grouper(freq='M', key='date'), columns='city')
print(df_group)
