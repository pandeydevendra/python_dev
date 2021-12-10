import pandas as pd

df = pd.read_csv("aapl.csv", parse_dates=["Date"], index_col="Date")
print(df.head(2))

print(df.index)

print(df['2017-06-30'])
print(df["2017-01"])

print(df['2017-06'].head())
print(df['2017-06'].Close.mean())
print(df['2017'].head(2))
print(df['2017-01-08':'2017-01-03'])
print(df['2017-01'])
print(df['Close'].resample('M').mean().head())

print(df['2016-07'])

# %matplotlib inline
# df['Close'].plot()

df = df['Close'].resample('M').mean().plot(kind='bar')
df.plot()


