a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

from itertools import chain

for x in chain(a, b):
    print(x)
