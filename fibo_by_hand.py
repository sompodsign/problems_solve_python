class Fibonacchi:

    def __iter__(self):
        return FibonacchiGenerator()

class FibonacchiGenerator:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self

##### pythonic fibonacchi
def fibonacchi():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

print(fibonacchi())
for i in fibonacchi():
    print(i)