"""
Lambda expression in Python
"""

#one parameter lambda (as a simple function)
x1 = "acer"
test1 = lambda a : a.upper()

print(f"test1: {test1(x1)}")

# condition check
test2 = lambda x2: "odd number" if x2 % 2 ==1 else "even number"
print(test2(6))

larger = lambda a, b : a if (a>b) else b
print(larger(1,2))

# loop
print ([x for x in range(1,5)])
