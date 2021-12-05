from itertools import combinations

items = ["a", "b", "c"]

for c in combinations(items, 3):
    print(c)

print("*"*100)

for c in combinations(items, 2):
    print(c)