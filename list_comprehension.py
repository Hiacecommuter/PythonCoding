"""
newlist = [expression for item in iterable if condition == True]
A list comprehension in Python works by loading the entire output list into memory.
map() also operates lazily
"""
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

#set comprehension
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}

#dict comprehension
squares = {i: i * i for i in range(10)}


#Walrus operator
import random
def get_weather_data():
    return random.randrange(90, 110)
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
hot_temps
[107, 102, 109, 104, 107, 109, 108, 101, 104]

"""
When the size of a list becomes problematic, 
it’s often helpful to use a generator instead of a list comprehension in Python

A generator doesn’t create a single, large data structure in memory, 
but instead returns an iterable. 
Your code can ask for the next value from the iterable as many times as necessary 
or until you’ve reached the end of your sequence, 
while only storing a single value at a time.
"""

