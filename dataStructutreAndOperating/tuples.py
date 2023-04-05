# Python 4 built-in data types tuple, list, set, and dict

# A tuple is a collection which is ordered and unchangeable. 
# Tuple allows duplicate values.
mytuple = ("apple", "banana", "cherry", "apple")

#length of tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# one item tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# a tuple can contain different data type
tuple1 = ("abc", 34, True, 40, "male")

#type
type(mytuple)

#tuple constructor
thistuple = tuple(("apple", "banana", "cherry"))

