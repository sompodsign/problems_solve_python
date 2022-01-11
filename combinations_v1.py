from itertools import combinations

s, k = "HACK", 4
s = sorted(list(s))

for i in range(1, k+1):
    for j in combinations(s, i):
        print("".join(j))

'''
A
C
H
K
AC
AH
AK
CH
CK
HK
'''