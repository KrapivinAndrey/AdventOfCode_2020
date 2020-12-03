with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]


dx = 3
length = len(in_data[0])
x = 0
trees = 0

for y in range(len(in_data)):
    if in_data[y][x] == "#":
        trees += 1
    x = (x + dx) % length

print(trees)
