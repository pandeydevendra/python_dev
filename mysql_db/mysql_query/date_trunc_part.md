# Standard Date Format:
YYYY-MM-DD hh:mm:ss
YEAR-MONTH-DAY HOUR:MINUTE:SECOND
2021-08-23 08:24:45

# Read DATE: DATE_TRUNC()
> DATE_TRUNC() reads full date in its standard format

DATE_TRUNC('day', date_column_name) AS day_wise                           day days don't make any difference here
2014-01-01T00:00:00.000Z	
2014-01-02T00:00:00.000Z
2014-01-03T00:00:00.000Z

DATE_TRUNC('month', created) AS month_wise
2014-01-01T00:00:00.000Z
2014-02-01T00:00:00.000Z
2014-03-01T00:00:00.000Z

DATE_TRUNC('year', occurred_at) AS year_wise
2014-01-01T00:00:00.000Z
2015-01-01T00:00:00.000Z
2016-01-01T00:00:00.000Z

DATE_TRUNC('hour', created_on) AS hour_wise
2014-01-01T10:00:00.000Z
2014-01-01T11:00:00.000Z
2014-01-01T13:00:00.000Z

DATE_TRUNC('minute', occurred_at) AS minute_wise
2016-05-01T15:55:00.000Z
2016-05-31T21:09:00.000Z
2016-05-31T21:22:00.000Z	

DATE_TRUNC('second', occurred_at) AS second_wise
2016-05-01T15:40:04.000Z
2016-05-01T15:55:51.000Z
2016-05-31T21:09:48.000Z
2016-05-31T21:22:48.000Z


# DATE_PART()
> DATE_PART() reads date specifically
> i.e day, or month, or year, or hour etc

DATE_PART('day', date_column_name) AS day                             day days don't make any difference here
we get a column name day from "1 to 31" with output as 
day
1
2	
3	
4	
5

DATE_PART('month', date_column_name) AS month
we get a column name month from "1 to 12" with output as 
month
1
2	
3	
4	
5

DATE_PART('year', date_column_name) AS year
we get a column name year as it is; with output as 
year
2014
2015
2016	

DATE_PART('hour', date_column_name) AS hour
we get a column hour from "0 to 23" with output as 
hour
0
1
3
4	

DATE_PART('minute', date_column_name) AS minute
we get minute from "0 to 59" with output as 
minute
0
1
3
4	 
Similary for second.. "0 to 59" from 0....                                day, days, minute, minutes all give same output


>Special: week and dow: date of week

DATE_PART('week', o.occurred_at) AS week
we get week from "1 to 52 or 53" such as
week
1
2
3
4

DATE_PART('dow', o.occurred_at) AS day_of_week
gives results on the scale of a week ie 7 days; "0 to 6" as:
day_of_week
0
1
2
3
4
5
6
