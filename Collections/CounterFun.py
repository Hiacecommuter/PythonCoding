"""
A Counter is a dict subclass for counting hashable objects. 
It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
Counts are allowed to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages."""
from collections import Counter
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

c = Counter(['eggs', 'ham'])
c['bacon']                              # count of a missing element is zero
#0

c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry

#methods
"""
https://docs.python.org/2/library/collections.html#collections.Counter
"""
