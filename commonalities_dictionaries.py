a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.values() and b.values())
print(a.items() & b.items())