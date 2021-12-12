import pandas as pd

df = pd.read_csv("msft.csv")
print(df)
print(df.index)

print(" ")
df = pd.read_csv("msft.csv", header=1, index_col='Date Time', parse_dates=True)
print(df)
print(df.index)

"""
Two types of datetimes in python:;
    <1> Naive (no timezone awareness
    <2>Timezone aware datetime
Convert naive DatetimeIndex to timezone aware DatetimeIndex using tz_localize
"""
df.tz_localize(tz='US/Eastern')
print(" ")
print(df)
print(" ")

df.index = df.index.tz_localize(tz='US/Eastern')
print(df.index)
print(" ")
# converting timezone:;
df_berlin = df.tz_convert('Europe/Berlin')
print(df_berlin)
print(df_berlin.index)
print(" ")
# All timetones:;
from pytz import all_timezones

print(all_timezones)


def all_timeozones():
    for value in all_timezones:
        if 'Asia' in value:
            print(value)
        else:
            pass


all_timeozones()
print(" ")
# convert to mumbai timezones:;
# df_mumbai = df.tz_convert('Asia/Mumbai')
'''
raise UnknownTimeZoneError(zone)
pytz.exceptions.UnknownTimeZoneError: 'Asia/Mumbai'

# tz_convertz database doesn't have any Mumbai timezone but calcutta and mumbai are both in same 
timezone so we will use that
'''
df_mumbai = df.tz_convert('Asia/Calcutta')
print(df_mumbai)
print(" ")

df.index = df.index.tz_convert('Asia/Calcutta')
print(df)
print(df.index)
print(" ")

# @ Using timezones in date_range:;

# 1) timezone using pytz

london = pd.date_range('3/6/2012 00:09:00', periods=10, freq='H', tz='Europe/London')
print(london)

# 2) timezones using dateutil:;

td = pd.date_range('3/6/2012 00:00', periods=10, freq='H', tz='dateutil/Europe/London')
print(td)

"""
Pandas documentation indicates that differences between pytz timezone and dateutil timezones are
    <1>  pytz you can find a list of common (and less common)
        timezones using from pytz import common_timezones, all_timezones
    <2> dateutil uses the OS timezones so there isn’t a fixed list available.
        For common zones, the names are the same as pytz.
"""
# Airthmetic between different timezones:;

df_rng = pd.date_range(start="2017-08-22 09:00:00", periods=10, freq='30min')
s = pd.Series(range(10), index=df_rng)
print(s)
print(" ")
df_rng = pd.date_range(start="2017-08-22 09:00:00", periods=10, freq='60min')
s = pd.Series(range(10), index=df_rng)
print(s)
print(" ")
b = s.tz_localize(tz="Europe/Berlin")
print(b)
print(b.index)

print(" ")
m = s.tz_localize(tz="Asia/Calcutta")
print(m.index)
print(m)
print(" ")
'''
It will first convert individual timezones to UTC and 
then align datetimes to perform addition/subtraction etc. operations
'''
t = b + m
print(t)
print(t.index)
