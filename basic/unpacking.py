"""
* can unpack any itrables
** only unpacks dictionaries
"""

my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
"""
1
[2, 3, 4, 5]
6
"""

# merge dicts
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}
print(my_merged_dict)

a = [*"RealPython"]

*a, = "RealPython"
# ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

*a, b = "RealPython"
# a : ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
# b : "RealPython"

