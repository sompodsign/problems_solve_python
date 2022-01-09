def producer(sentence, next_coroutine):
    '''Producer which just split strings and feed it to pattern filter courine'''
    tokens = sentence.split()
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    """
    Search for pattern in received token and if pattern got matched
    send to to print_token() coroutine for printing
    :param pattern:
    :param next_coroutine:
    :return:
    """
    print("Search for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print('Done with filtering!')


def print_token():
    """Act as a sink, simply print the received tokens"""
    print("I'm sink, I'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


pt = print_token()
next(pt)
pf = pattern_filter(next_coroutine=pt)
next(pf)

sentence = "Bobn is running behind a fast moving car"
producer(sentence, pf)
