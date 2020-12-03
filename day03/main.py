with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]

length = len(in_data[0])


def count_trees(dx, dy):
    x = y = trees = 0
    while y < len(in_data):
        if in_data[y][x] == "#":
            trees += 1
        x = (x + dx) % length
        y += dy

    return trees


res = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)
print(res)
