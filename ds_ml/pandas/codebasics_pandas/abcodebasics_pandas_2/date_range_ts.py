import pandas as pd
import numpy as np


df = pd.read_csv("aapl_no_dates.csv")
df.head()

rng = pd.date_range(start="6/1/2016",end="6/30/2016",freq='B')
rng

df.set_index(rng, inplace=True)
df.head()

daily_index = pd.date_range(start="6/1/2016",end="6/30/2016",freq='D')
daily_index

daily_index.difference(df.index)

# %matplotlib inline
# df.Close.plot()

df["2016-06-01":"2016-06-10"].Close.mean()
df.index

df.asfreq('D',method='pad')

df.asfreq('W',method='pad')
df.asfreq('H',method='pad')

rng = pd.date_range('1/1/2011', periods=72, freq='H')
rng

ts = pd.Series(np.random.randint(0,10,len(rng)), index=rng)
ts.head(20)
