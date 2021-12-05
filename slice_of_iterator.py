import itertools


def count(n):
    while True:
        n += 1
        yield n


c = count(0)

for x in itertools.islice(c, 10, 20):
    print(x)
