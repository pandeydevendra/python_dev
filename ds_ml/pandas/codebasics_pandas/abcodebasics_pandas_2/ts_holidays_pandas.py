import pandas as pd
df = pd.read_csv("aapl_no_dates.csv")
df.head()

rng = pd.date_range(start="7/1/2017", end="7/21/2017", freq='B')
rng

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

us_cal = CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng = pd.date_range(start="7/1/2017",end="7/23/2017", freq=us_cal)
rng

df.set_index(rng,inplace=True)
df.head()

from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday


class myCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birth Day', month=4, day=15),  # , observance=nearest_workday),
    ]


my_bday = CustomBusinessDay(calendar=myCalendar())
pd.date_range('4/1/2017', '4/30/2017', freq=my_bday)

egypt_weekdays = "Sun Mon Tue Wed Thu"

b = CustomBusinessDay(weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)

b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)

from datetime import datetime
dt = datetime(2017,7,9)
dt

dt + 1*b