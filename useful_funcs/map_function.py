"""
map function in Python

map(func, iter) function executes a specifiied function for each item for an iterable.

map() also operates lazily
"""

print(map(lambda a: a*2, (1,2,3,4))
      
print(map(lambda x, y: x+y, [1,2,3,4,5], [10, 20, 30, 40, 50]))
      
print(map(int, ['1', '2', '3']))
