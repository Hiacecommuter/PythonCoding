# return elements with an index fro iterable objects
for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie

#set start num
for i, name in enumerate(l, 1):
    print(i, name)
# 1 Alice
# 2 Bob
# 3 Charlie

for i, name in enumerate(l, 42):
    print(i, name)
# 42 Alice
# 43 Bob
# 44 Charlie

#change format
for i, name in enumerate(l, 1):
    print('{:03}_{}'.format(i, name))
# 001_Alice
# 002_Bob
# 003_Charlie

step = 3
for i, name in enumerate(l):
    print(i * step, name)
# 0 Alice
# 3 Bob
# 6 Charlie
