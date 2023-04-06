#1 Function

#2 Scope 
'''In Python functions create a new scope. 
This means Python looks first in the namespace of the function to find variable names 
when it encounters them in the function body. '''

a_string = "This is a global variable"
def foo():
...     print locals()
print globals() # doctest: +ELLIPSIS
#{..., 'a_string': 'This is a global variable'}
foo() # 2
#{}

#3 variable resolution rules
a_string = "This is a global variable"
def foo():
     a_string = "test" # 1
     print locals()
foo()
#{'a_string': 'test'}
a_string # 2
#'This is a global variable'

#4 variable lifetime

#5 function arguments and parameters
"""Python does allow us to pass arguments to functions. 
The parameter names become local variables in our function."""
def foo(x):
     print locals()
foo(1)
#{'x': 1}

#6 nested functions
def outer():
     x = 1
     def inner():
         print x # 1
     inner() # 2

outer()
# 1

#7 functions are first class objects in python
'''functions are objects in Python, just like everything else'''

#8 closures
'''
Python supports a feature called function closures 
which means that inner functions defined in non-global scope remember 
what their enclosing namespaces looked like at definition time. 
This can be seen by looking at the func_closure attribute of our inner function 
which contains the variables in the enclosing scopes.
'''

#9 decorators
'''
A decorator is just a callable that takes a function as an argument 
and returns a replacement function.'''
def outer(some_func):
     def inner():
         print "before some_func"
         ret = some_func() # 1
         return ret + 1
     return inner
def foo():
     return 1
decorated = outer(foo) # 2
decorated()
#before some_func
#2
#We could say that the variable decorated is a decorated version of foo
#calls to foo() won’t get the original foo, they’ll get our decorated version!
foo = outer(foo)#replace foo with the decorated version altogether

#10 The @ symbol applies a decorator to a funtion
add = wrapper(add)
@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)
#this is no different than simply replacing the original variable add 
#with the return from the wrapper function 

#11 *arg and **kwargs
'''*args means either extract positional variables from an iterable 
if calling a function or 
when defining a function accept any extra positional variables.'''
def add(x, y):
    return x + y
lst = [1,2]
add(lst[0], lst[1]) # 1
#3
add(*lst) # 2 unpack
#3

def one(*args):
    print args # 1
one()
#()
one(1, 2, 3)
#(1, 2, 3)
def two(x, y, *args): # 2
    print x, y, args
two('a', 'b', 'c')
#a b ('c',)

#** which does for dictionaries & key/value pairs exactly what * does for iterables and positional parameters
def foo(**kwargs):
    print kwargs
foo()
#{}
foo(x=1, y=2)
#{'y': 2, 'x': 1}

dct = {'x': 1, 'y': 2}
def bar(x, y):
    return x + y
bar(**dct)
#3


#http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
