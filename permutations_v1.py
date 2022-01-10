from itertools import permutations

s, k = "HACK", 2

for i in permutations(s, int(k)):
    print(i)