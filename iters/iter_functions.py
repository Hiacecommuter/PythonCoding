from itertools import product
A = (1, 2)
B = (3, 4)
print(*(product(A, B))) #(1, 3) (1, 4) (2, 3) (2, 4)

