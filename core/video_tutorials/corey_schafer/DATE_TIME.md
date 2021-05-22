>>> from datetime import datetime
>>> first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
>>> print(first_date)
2014-07-01 00:00:00
> 
> Date and Time Formatting Arguments from the datetime Module
Argument Meaning
%A Weekday name, such as Monday
%B Month name, such as January
%m Month, as a number (01 to 12)
%d Day of the month, as a number (01 to 31)
%Y Four-digit year, such as 2015
%y Two-digit year, such as 15
%H Hour, in 24-hour format (00 to 23)
%I Hour, in 12-hour format (01 to 12)
%p am or pm
%M Minutes (00 to 59)
%S Seconds (00 to 61)

Plotting Dates
Knowing how to process the dates in our CSV file, we can now improve our
