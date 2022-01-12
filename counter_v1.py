from collections import Counter

number_of_shoes = int(input())
shoe_sizes = Counter(list(map(int, input().split())))
number_of_customers = int(input())

earnings = 0
for x in range(number_of_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1
print(earnings)