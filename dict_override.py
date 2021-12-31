class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


import collections

class DoppelDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 4)

d = DoppelDict({"one": 1})
print(d)
d1 = DoppelDict({"two": 2})
print(d1)