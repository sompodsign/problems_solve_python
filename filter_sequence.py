mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

pos = (n for n in mylist if n > 0)  # Generator expression

for x in pos:
    print(x)

## filter
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
# print(ivals)

# list comprehension
clip_neg = [n if n > 0 else 0 for n in mylist]
# print(clip_neg)
