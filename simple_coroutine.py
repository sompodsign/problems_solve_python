def simple_coroutine():
    print('-> Coroutine started')
    x = yield
    print('-> Coroutine received:', x)

my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
my_coro.send(42)