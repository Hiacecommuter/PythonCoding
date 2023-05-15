"""
With statement 
"""

"""
resource management
Ensures that open file descriptors are closed automatically after program leaves the context of the with
"""
with open('hello.txt', 'w') as f:
    f.write('hello, world!')
 

some_lock = threading.Lock()

# Harmful:
some_lock.acquire()
try:
    # Do something...
finally:
    some_lock.release()

# Better:
with some_lock:
    # Do something...    
    

"""
context managers
__enter__ : enters the context, acquire the resource
__exit__ : free up the resource.
"""
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            
            with ManagedFile('hello.txt') as f:
f.write('hello, world!')
f.write('bye now')

# https://dbader.org/blog/python-context-managers-and-with-statement
