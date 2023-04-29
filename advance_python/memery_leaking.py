# cyclic dependency 
a1 = ['a', 'b']
a2 = [ 1, 2]
a1.append(a2)
a2.append(a1)
del a1
del a2
