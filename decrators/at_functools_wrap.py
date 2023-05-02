"""
to make __name__ to decorated function to itselt

The @functools.wraps decorator uses the function functools.update_wrapper() 
to update special attributes like __name__ and __doc__ that are used in the introspection.
"""
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
  
@do_twice    
def say_whee():
    print("Whee!")
say_whee()   
print(say_whee.__name__)    #  say_whee
