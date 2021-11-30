from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Brazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))  # itemgetter can take multiple keys as argument


# alternative
rows_by_fname_lname = sorted(rows, key=lambda r: (r['fname'], r['lname']))