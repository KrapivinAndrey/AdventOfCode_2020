import numpy as np

matrix = np.zeros((50, 50, 50, 50))

with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.readlines()]


def count_neighbors(x, y, z, w, matrix):
    result = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == j == k == l == 0:
                        continue
                    if matrix[x + i, y + j, z + k, w + l] == 1:
                        result += 1
    return result


def move(temp, radius):
    result = np.zeros((50, 50, 50, 50))
    for x in range(25-radius-1, 25 + radius + 2):
        for y in range(25-radius-1, 25 + radius + 2):
            for z in range(25-radius-1, 25 + radius + 2):
                for w in range(25-radius-1, 25 + radius + 2):
                    if temp[x, y, z, w] == 1 and count_neighbors(x, y, z, w, temp) in [2, 3]:
                        result[x, y, z, w] = 1
                    elif temp[x, y, z, w] == 0 and count_neighbors(x, y, z, w, temp) == 3:
                        result[x, y, z, w] = 1
    print(np.count_nonzero(result))
    return result


radius = len(in_data) // 2
print(radius)
for i in range(len(in_data)):
    for j in range(len(in_data)):
        if in_data[i][j] == '#':
            matrix[25-radius+i, 25-radius+j, 25, 25] = 1

for i in range(6):
    matrix = move(matrix, radius)
    radius += 1
