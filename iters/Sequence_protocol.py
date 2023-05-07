""" 
  sequence protocol, which consists of the following methods:

.__getitem__(index) takes an integer index starting from zero and returns the items at that index in the underlying sequence. It raises an IndexError exception when the index is out of range.
.__len__() returns the length of the sequence.
"""

"""
A quick way to create an .__iter__() method is to take advantage of the built-in iter() function, which returns an iterator out of an input data stream
"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None

    def __iter__(self):
        return iter(self._items)
      
class Stack:
    # ...

    def __iter__(self):
        for item in self._items:
            yield item      
