prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
tech_names = {'AAPL', 'IBM', 'HPQ', 'FB'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)