import pandas as pd

df = pd.read_csv("fb.csv") # ,parse_dates=['Date'],index_col='Date')
print(df)
print(" ")
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col='Date')
print(df)
print(" ")

# Shift values:;

print(df.shift(1)) # forward shifting
print(" ")
print(df)
print(" ")
print(df.index)
print(df.shift(-1))
print(" ")

df["Prev Day Price"] = df['Price'].shift(1)
print(df)

print(" ")
df['Price Change'] = df['Price'] - df['Prev Day Price']
print(df)

print(" ")
df['5 day return'] =  (df['Price'] - df['Price'].shift(5))*100/df['Price'].shift(5)
print(df)
print(" ")
df = df[['Price']]
print(df)
print(" ")

# time/date shifting:;
print(df.index)
print(" ")
df.index = pd.date_range(start='2017-08-15',periods=10, freq='B')
print(df)
print(" ")

df.index
print(df.tshift(1)) # t with shift makes tshift is for time shift
print(" ")
print(df.tshift(-1))

print(df.tshift(-2))

print(df)
print(df.index)