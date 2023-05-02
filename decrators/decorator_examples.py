"""pass a function as a parameter
referencing a function  -- just function name no parenthesis
call a function -- function name with parenthesis
"""

"""inner functions
functions are defined inside other functions
Cannot directly access inner functions
"""

""" Returning functions from functions
inner function can be return and use in the future
"""
def test1():
  def add(a, b):
    return a+b
  return add
  
func = test1()
print(func(1,2)

""" Simply decorator
decorators wrap a function, modifying its behavior.
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)   # say_whee points to the inner function wrapper

""" a simple way to use decorator
@
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
