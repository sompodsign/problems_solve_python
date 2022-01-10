from itertools import product

A = [1, 2]
B = [3, 4]

for i in product(A,B):
    print(i, end=' ')