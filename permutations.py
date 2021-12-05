import itertools

items = ["a", "b", "c"]

for p in itertools.permutations(items):
    print(p)

#############
print("----------------------**********************------------------------")
for p in itertools.permutations(items,2):
    print(p)