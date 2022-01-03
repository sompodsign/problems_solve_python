import itertools

gen = itertools.takewhile(lambda x: x < 3, itertools.count(1, .5))
print(list(gen))

sample = [5,3,4,5,6,7,3,4,5]
list(itertools.accumulate(sample))
list(itertools.accumulate(sample, min))
list(itertools.accumulate(sample, max))

list(itertools.chain('ABC', range(2)))
list(itertools.chain(enumerate('ABC')))

list(itertools.chain.from_iterable(enumerate('ABC')))

list(itertools.product('ABC', repeat=2))

ct = itertools.count()
next(ct)

list(itertools.islice(itertools.count(1, .3), 3))

all([1,2,3])
all([1,0,3])
any([1,2,3])
any([0, 0.0])

g = (n for n in [0,0.0, 7, 8])
print(g)
any(g)