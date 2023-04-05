# can zip multiple iterable togeter, return lenght is determined by the shortest one
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
points = [100, 85, 90]

for name, age, point in zip(names, ages, points):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 90

#In the case that number of elements is different, zip() ignores the extra elements

# strict parameter of zip()
# If strict=True, an error is raised if the number of elements is different.
# ValueError: zip() argument 2 is shorter than argument 1

# use the longest one, and fill missing values with any values
#itertools.zip_longest(), default value is None
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip_longest(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
# Dave None

for name, age in zip_longest(names, ages, fillvalue=20):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
# Dave 20
