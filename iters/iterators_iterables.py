"""
A Python object is an iterator when it implements iterator protocol:
.__iter__() : Called to initialize the iterator. It must return an iterator object
.__next__() : Called to iterate over the iterator. It must return the next value in the data stream
Use iter() and next() in code
"""

"""
The only responsibility of __iter__() is to return an iterator oject.
The .__iter__() method of an iterator typically return self, which holds a reference to the iterator itself

def __iter__(self):
  return self
  
__next__() method raises a StopIteration exception when no more items are available in the data stream  
"""

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
            
for item in SequenceIterator([1, 2, 3, 4]):
    print(item) 
    
# infinite iterators, generating new data
class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration  
            
""" Inheriting From collections.abc.Iterator
The collections.abc module includes an abstract base class (ABC) called Iterator.
This class provides basic implementations for the .__iter__() method.
It also provides a .__subclasshook__() class method that ensures only classes implementing the iterator protocol will be considered subclasses of Iterator
If you inherit from Iterator, then you don’t have to write an .__iter__() method because the superclass already provides one with the standard implementation.
"""
from collections.abc import Iterator

class SequenceIterator(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

for number in SequenceIterator([1, 2, 3, 4]):
   print(number)

"""
It’s important to note that .__iter__() is semantically different for iterables and iterators. 
In iterators, the method returns the iterator itself, which must implement a .__next__() method. 
In iterables, the method should yield items on demand.
"""
