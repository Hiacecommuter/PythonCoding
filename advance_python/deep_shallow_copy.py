"""
Assignment statements in Python do not create copies of objects, they only bind names to an object.
"""
"""
A shollow copy means constructing a new collection object and then populating it with references
to the child objects found in the original. In essence, a shallow copy is only one level deep. 
The copying process does not recurse and therefore won't create copies of the child objects themselves

A deep copy makes the copying process recursive. It means first constructing a new collection object
and them recursively populating it with copies of the child objects found in the original.
Copying an object his way walks the whole object tree to create a fully independent clone of the 
original object and all of its children.
"""

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy

import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
