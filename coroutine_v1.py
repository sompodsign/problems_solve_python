def print_name(prefix):
    print("Searching prefix: {}".format(prefix))

    while True:
        name = (yield)
        if prefix in name:
            print(name)

corou = print_name('Dear')
corou.__next__()
corou.send('Dear Shampad')
