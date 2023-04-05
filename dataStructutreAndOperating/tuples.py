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

#index tuple, same as list
thistuple = ("apple", "banana", "cherry")
thistuple[1]

# tuple is unchangeable, but they can be appended 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

#!!!!If the number of variables is less than the number of values,
#you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
