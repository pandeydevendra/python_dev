import pandas as pd

dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05', '20170105']
df = pd.to_datetime(dates)
print(df)

dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05', '20170105']
df = pd.to_datetime(dt)
print(df)

print(pd.to_datetime('30-12-2016'))

df = pd.to_datetime('5-1-2016', dayfirst=True)
print(df)
df = pd.to_datetime('2017$01$05', format='%Y$%m$%d')
print(df)

df = pd.to_datetime('2017#01#05', format='%Y#%m#%d')
print(df)
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore')
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce')

current_epoch = 1501324478
pd.to_datetime(current_epoch, unit='s')

pd.to_datetime(current_epoch * 1000, unit='ms')

t = pd.to_datetime([current_epoch], unit='s')
t

t.view('int64')
