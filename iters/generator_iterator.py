"""
Generators refer to generator function and generator iterator
yield is an expression, rather than a statement
"""

def sequence_generator(sequence):
    for item in sequence:
        yield item
"""
Internally, the iterator will run the original loop, 
yielding items on demand until the loop consumes the input sequence, 
in which case the iterator will automatically raise a StopIteration exception
"""
for number in sequence_generator([1, 2, 3, 4]):
    print(number)
    



