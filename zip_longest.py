a = [1,2,3]
b = ['w', 'x', 'y', 'z']

from itertools import zip_longest

for i in zip_longest(a,b, fillvalue=0):
    print(i)