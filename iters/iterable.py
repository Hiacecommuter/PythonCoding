"""
The iterable protocol consists of a single special method.
The  .__iter__() method fulfills the iterable protocol. 
This method must return an iterator oject, which usually does not coincide with self, unless the iterable is an iterator.
"""

"""
You can add a .__next__() method to a custom iterable and return self from its .__iter__() method. 
This will turn your iterable into an iterator on itself. 
However, this addition imposes some limitations. 
The most relevant limitation may be that you won’t be able to iterate several times over your iterable.
"""

from sequence_iter import SequenceIterator

class Iterable:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return SequenceIterator(self.sequence)

from sequence_iterable import Iterable

for value in Iterable([1, 2, 3, 4]):
    print(value)      

""" unpack iterable
*iterable
"""
