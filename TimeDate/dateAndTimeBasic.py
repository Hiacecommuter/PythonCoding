"""
Unix epoch 00:00:00 UTC 1st Jan 1970. 
UTC stands for Coordinated Universal Tine or Greenwich Mean time (GMT)

The IANA maintains a database of all the values of time zone offsets.

YYYY-MM-DD HH:MM:SS format for year, month, day, hour, minute, and second
"""
import time

time.time()  #number of seconds since the epoch

"""
datetime provides three classes 
 1 - datetime.date is an idealized date that the Gregorian calendar extends infinitely into the future and past.
     This object stores the year, month, and day as attributes
 2 - datetime.time is an idealized time that assumes there are 86.400 seconds perday with no leap seconds.
     This object stores the hour, minute, second, microsecond, and tzinfo (time zone information)
 3 - datetime.datetime is a combination of a date and a time. It has all the attributes of boht classes.
 """
 
from datetime import date, time, datetime

date(year=2020, month=1, day=31)
# datetime.date(2020, 1, 31)

time(hour=13, minute=14, second=31)
# datetime.time(13, 14, 31)

datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)
# datetime.datetime(2020, 1, 31, 13, 14, 31)

today = date.today()

# datetime.date(2020, 1, 24)

now = datetime.now()
# datetime.datetime(2020, 1, 24, 14, 4, 57, 10015)

current_time = time(now.hour, now.minute, now.second)
datetime.combine(today, current_time)
# datetime.datetime(2020, 1, 24, 14, 4, 57)

### Using Strings to Create Python datetime Instances
date.fromisoformat("2020-01-31")
# datetime.date(2020, 1, 31)

date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"

datetime.strptime(date_string, format_string)
# datetime.datetime(2020, 1, 31, 14, 45, 37)
