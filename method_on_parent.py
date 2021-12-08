class A:
    def spam(self):
        print('A.spam')


class B(A):
    def span(self):
        print('B.spam')
        super().spam()


b = B()
b.spam()


#################
class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
#################
