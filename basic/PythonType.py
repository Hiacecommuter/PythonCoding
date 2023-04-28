"""
Built-in Data Types in Python consist of 
    Text Type: str
    Numeric Types: int, float, complex
    Sequence Types: list, tuple, range
    Mapping Type: dict
    Set Types: set, frozenset
    Boolean Type: bool
    Binary Types: bytes, bytearray, memoryview
    None Type: None

    reference: https://www.w3schools.com/python/python_datatypes.asp
"""

#declare the type of returned value for a function

def greeting(name:str) -> str:
    return 'Hello ' + name

print(greeting('Max'))

#set vs frozenset
#set: unordered, unindexed, and mutable; no hash values
#change the elements using add(), remove(), discard()
#remove() vs discard(): if item does not exit, the remove() method will raise an error but discard will not
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
print(type(fruits), end="--")
print(fruits)
fruits.add("Orange")
print(fruits)
fruits.remove("Apple")
print(fruits)
fruits.discard("Apple")
print(fruits)
fruits.discard("Banana")
print(fruits)
#frozenset: unordered, unindexed, and immutable; hashable
#two frozensets can be combined(|), intersected(&), or differentiated (-)
#Reference: https://www.python-engineer.com/posts/set-vs-frozentset/


