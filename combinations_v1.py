from itertools import combinations

s, k = "HACK", 2
s = sorted(list(s))

for i in sorted(combinations(s, 1)):
    print(''.join(i))
for i in combinations(s, k):
    print("".join(i))

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