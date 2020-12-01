from itertools import product

with open('input.txt', 'r') as reader:
    in_data = [int(x) for x in reader.read().split('\n')]

answer = [x * y for x, y in product(in_data, in_data) if x+y == 2020]

# first
print(*answer)

answer = [x * y * z for x, y, z in product(in_data, in_data, in_data) if x+y+z == 2020]

# second
print(*answer)