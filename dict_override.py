class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


if __name__ == '__main__':
    d = DoppelDict(one=1)
    print(d)
    d['two'] = 2
    print(d)