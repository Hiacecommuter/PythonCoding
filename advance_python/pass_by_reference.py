"""
Python passes arguments by assignment.
"""

# variable changes after reassignment
def increment(a):
  print(id(a))
  a = a+1
  print(id(a))
x= 1
print(id(x))   
increment(x) 

"""
identifier
sys.getrefcount() -- obtain the reference counts for arbitrary values

Let’s stick to the x = 2 example and examine what happens when you assign a value to a new variable:
If an object representing the value 2 already exists, then it’s retrieved. Otherwise, it’s created.
The reference counter of this object is incremented.
An entry is added in the current namespace to bind the identifier x to the object representing 
This entry is in fact a key-value pair stored in a dictionary! 
A representation of that dictionary is returned by locals() or globals().
"""

"""
Function arguments in Python are local variables. 
locals(), globals()
"""

"""
pass by reference
1. use global keyword, not recommend
2. use return and reassgin best practice
"""

"""
Additionally, you should be mindful of class attributes. 
They will remain unchanged, and an instance attribute will be created and modified
---
Since class attributes remain unchanged when modified through a class instance, 
you’ll need to remember to reference the instance attribute.
"""

"""
dict is only standard mapping type
An object is subscriptable when a subset of its structure can be accessed by index positions
an object is mutable if its structure can be changed in place rather than requiring reassignment
"""

