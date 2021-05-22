from datetime import datetime, date, timedelta

datetime_object = datetime.now()
print(datetime_object)

date_today = date.today()
print(date_today)
"""
date before 2 days
"""
t = timedelta(days=2)
d_2_date = date_today - t
print(d_2_date)

"""
date after 7 days = 1 week
"""
t1 = timedelta(weeks=1)
d_7_date = date_today + t1
print(d_7_date)

# date object of today's date
t_d_m = datetime.now()
print(t_d_m, type(t_d_m))

print("Current year:", t_d_m.year, type(t_d_m.year))
print("Current month:", t_d_m.month, type(t_d_m.month))
print("Current day:", t_d_m.day, type(t_d_m.day))
print("Current hour:", t_d_m.hour, type(t_d_m.hour))
print("Current minute:", t_d_m.minute, type(t_d_m.minute))
print("Current second:", t_d_m.second, type(t_d_m.second))
print("Current microsecond:", t_d_m.microsecond, type(t_d_m.microsecond))

"""
convert date/time into string
"""
date_today = date.today()
print(date_today, type(date_today))
date_today_str = date_today.strftime("%Y-%m-%d")
print(date_today_str, type(date_today_str))
