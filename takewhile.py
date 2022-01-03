import itertools

gen = itertools.takewhile(lambda x: x < 3, itertools.count(1, .5))
print(list(gen))