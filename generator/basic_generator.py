"""
Calling a generator function or use a generator expression, it returns a special iterator called a generator.
Generator functions are a special kind of function that return a lazy iterator.
Generator expression or generator comprehension
Generator is memory efficient but not time efficient
Generator can be exhausted
"""

"""
next() can receive parameter as returned value when the generator is exhausted
"""

""" Readin large files
"""

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

""" Generating an infinite sequence
"""

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")

gen = infinite_sequence()
next(gen)   # 0
next(gen)   # 1

""" yield
Yield indicates where a value is sent back to the caller.
Then the state of the function is remembered.
"""
