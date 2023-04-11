# example
'{} {}'.format('Python', 'Format')
'{1} {0}'.format('Python', 'Format')

# Value conversion:
class Data(object): # stepup

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'
x='{0!s} {0!r}'.format(Data()) # !s for str(), !r for repr(), in % style, use %s, %r

class Data(object):

    def __repr__(self):
        return 'räpr'
x='{0!r} {0!a}'.format(Data()) # uses ascii

#Padding and aligning strings:
# < -L, > -R, ^ -M
'{:>15}'.format('Python')
# supply padding value as an argument
'{:<{}s}'.format('Python', 15)
# change padding characters
'{:*<15}'.format('Python')

#Truncating long strings
'{:.10}'.format('Python Tutorial')
'{:.{}}'.format('Python Tutorial', 10)

#Combining truncating and padding
'{:10.10}'.format('Python')

# integers, floats
'{:d}'.format(24)
'{:f}'.format(5.12345678123)

# padding numbers
'{:5d}'.format(24)
'{:05.2f}'.format(5.12345678123)

# Signed numbers
#https://www.w3resource.com/python/python-format.php

# Named placeholders
data = {'first': 'Place', 'last': 'Holder!'}
'{first} {last}'.format(**data)

#Datetime
from datetime import datetime
'{:%Y-%m-%d %H:%M}'.format(datetime(2016, 7, 26, 3, 57))
#'2016-07-26 03:57'


