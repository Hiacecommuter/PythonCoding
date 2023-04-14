"""
Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted.
When iterating over an ordered dictionary, the iterms are returned in the order their theys were first added.
"""
from collections import OrderedDict
# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
#OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
#OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
#OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

# https://docs.python.org/2/library/collections.html#ordereddict-objects

### dictionary.get(keyname, value)
### key is required, value is optional -- a value to return if the specified key does not exit. Default None
"""
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
"""
from collections import OrderedDict
import re
N = int(input())
datas = OrderedDict()
for _ in range(N):
    [text, num] = re.split(r"\s(?=\d)",input())
    datas[text] = datas.get(text, 0) + int(num)
for i in datas:
    print(i,datas[i], sep=" ")
