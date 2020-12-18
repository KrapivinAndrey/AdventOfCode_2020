import numpy as np

matrix = np.zeros((100, 100, 100))

with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.readlines()]


def count_neighbors(x,y,z,matrix):
    result = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue
                if matrix[x+i,y+j,z+k] == 1:
                    result += 1

    return result


def move(matrix):
    result = np.zeros((100, 100, 100))
    for x in range(1, 99):
        for y in range(1, 99):
            for z in range(1, 99):
                if matrix[x, y, z] == 1 and count_neighbors(x, y, z, matrix) in [2, 3]:
                    result[x, y, z] = 1
                elif matrix[x, y, z] == 0 and count_neighbors(x, y, z, matrix) == 3:
                    result[x, y, z] = 1
    return result


for i in range(len(in_data)):
    for j in range(len(in_data)):
        if in_data[i][j] == '#':
            matrix[50+i, 50+j, 50] = 1

for i in range(6):
    matrix = move(matrix)

print(np.count_nonzero(matrix))