""" Native and aware object
A native object does not contain enough information to unambiguously locate itself to other date/time object
An aware object can locate itself relative to other aware object.
An aware object represents a specific moment in time.
"""

"""
For applications requiring aware objects, 
datetime and time objects have an optional time zone information attribute, 
tzinfo, that can be set to an instance of a subclass of the abstract tzinfo class. 
These tzinfo objects capture information about the offset from UTC time, 
the time zone name, and whether daylight saving time is in effect.
"""

""" Types
class datetime.date
      attributes: year, month, day
class datetime.time
      attributes: hour, minute, second, microsecond, tzinfo
class datetime.datetime
      attributes: year, month, day, hour, minute, second, microsecond, tzinfo
class datetime.tzinfo
      an abstract base class for time zone
class datetime.timezone      
      a class that implemets the tzinfo abstract base class as a fixed offset from the UTC
"""

"""subclass relationship
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
"""

