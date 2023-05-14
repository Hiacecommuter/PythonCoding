from datetime import datetime

# 1 datetime class
dt = datetime.now()
print(dt,       dt.year,   dt.month,  dt.day,
      dt.hour,  dt.minute, dt.second, sep = " ")    # attributes

# 2 get day of month and day of week
print(dt.day)
print(dt.weekday())
import calendar
print(calendar.day_name[dt.weekday()])

# 3 get week of the year
print(dt.isocalendar()) # iso calender, Mon is 1, datetime calender, Mon is 0

# 4 timestamp and vice verse
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))

# 5 time delta
from datetime import timedelta
print(timedelta(weeks=10, days=1))

dt1 = datetime.now()
import time
time.sleep(1)
dt2 = datetime.now()
print(dt2 - dt1)

# 6 string to datetime and vice verse
#strftime() and strptime()

# 7 time zone
from pytz import timezone
east = timezone('US/Eastern')
loc_dt = east.localize(datetime(2011, 11, 2, 7, 27, 0))
kolkata = timezone("Asia/Kolkata")
loc_dt.astimezone(kolkata)

# 8 pandas time
# to_datetime(): Converts string dates and times into Python datetime objects.
# to_timedelta(): Finds differences in times in terms of days, hours, minutes, and seconds.

# 9 Get Year, Month, Day, Hour, Minute in pandas
# dt: We can get year, month, day, hour, or minute from dates in a column of a pandas dataframe using dt attributes for all columns
date = pd.to_datetime("8th of sep, 2019")
date_series = date + pd.to_timedelta(np.arange(12), 'D')
date_series = pd.date_range('08/10/2019', periods = 12, freq ='D')

df = pd.DataFrame()
df['date'] = date_series
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute

df['weekday'] = df['date'].dt.weekday
df['day_name'] = df['date'].dt.weekday_name
df['dayofyear'] = df['date'].dt.dayofyear

df.index = df.date

# 10 time difference in seconds
"""
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000 25200

Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000  88200
"""
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    td = t1 - t2
    print(type(td))
    return str(int(abs(td.total_seconds())))
