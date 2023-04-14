"""
collections.namedtuple(typename, field_names[, verbose = False][,rename = False])
return a new tuple subclas named typename. 
The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup
as well as being indexable and iterable.

""
"""
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
"""

from collections import namedtuple
N = int(input())

student = namedtuple("student", input().rstrip())
content = []
for _ in range(N):
    content.append(student(*(input().rstrip().split())))
tot = 0.0
for i in content:
    tot+= float(i.MARKS)

print(round(tot/len(content), 2))
