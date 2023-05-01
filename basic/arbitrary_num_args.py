"""
In Python, a function can collect an arbitrary number of args
"""

# better use args other than toppings
def greet(a, *toppings):    # place last, store in a tuple
  print(type(toppings))
  print(toppings)
  print(*toppings)

greet("Jack", "Amy", "Bob", "Charlie") 
"""
<class 'tuple'>
('Amy', 'Bob', 'Charlie')
Amy Bob Charlie
"""

""" Using arbitrary keyword argument
use a dict to store argument name and value
"""

# better to use kwargs other than names
def greet_title(a, **names):
  print(type(names))
  for key, val in names.items():
    print(key, val)
    
greet_title("Jack", Dr = "Amy", Mr = "Bob", Sir = "Charlie")  
"""
<class 'dict'>
Dr Amy
Mr Bob
Sir Charlie
"""

"""Order of arguments
1. Standard arguments
2. *args arguments
3. **kwargs arguments
"""
