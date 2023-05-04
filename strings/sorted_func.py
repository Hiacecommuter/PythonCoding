#sorted(iterable, key=None, reverse=False)
"""
A list also has the sort() method which performs the same way as sorted(). 
The only difference is that the sort() method doesn't return any value and changes the original list.
"""

#key Parameter in Python sorted() function
sorted(iterable, key=len)

#having a key function
# take the second element for sort
def take_second(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sorted_list = sorted(random, key=take_second)

#Sorting with multiple keys
"""
Two tuples can be compared by comparing their elements starting from first. 
If there is a tie (elements are equal), the second element is compared, and so on.
"""
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]
def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)
sorted_list = sorted(participant_list, key=sorter)
sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))

#https://www.programiz.com/python-programming/methods/built-in/sorted

string = "cab"
print(sorted(string))   # ['a', 'b', 'c']
