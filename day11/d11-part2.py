import numpy as np
with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]

length = len(in_data[0])
height = len(in_data)

seat_map = np.chararray(shape=(length, height))
for i in range(height):
    seat_map[i] = np.array(list(in_data[i]))

print(seat_map)


def calculate(matrix):
    res = np.zeros(shape=(length, height))
    direction = [ (-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]

    for i in range(length):
        for j in range(height):
            if matrix[j][i] == b'.':
                res[j][i] = -1
            else:
                occupied = 0
                for dir in direction:
                    stop = False
                    x = i + dir[0]
                    y = j + dir[1]
                    while not stop:

                        if x == -1 or y == -1:
                            stop = True
                        elif x == length or y == height:
                            stop = True
                        elif matrix[y][x] == b"#":
                            stop = True
                            occupied += 1
                        elif matrix[y][x] == b"L":
                            stop = True
                        else:
                            x = x + dir[0]
                            y = y + dir[1]

                res[j][i] = occupied

    return res


def new_seat(calc, matrix):
    flag = False
    res = np.chararray(shape=(length, height))
    for i in range(length):
        for j in range(height):
            if calc[j][i] == -1:
                res[j][i] = b'.'
            elif matrix[j][i] == b'L' and calc[j][i] == 0:
                res[j][i] = b'#'
                flag = True
            elif matrix[j][i] == b'#' and calc[j][i] >= 5:
                res[j][i] = b'L'
                flag = True
            else:
                res[j][i] = matrix[j][i]

    return res, flag


flag_changed = True
while flag_changed:
    temp = calculate(seat_map)
    temp_seat, flag_changed = new_seat(temp, seat_map)
    seat_map = temp_seat

print((temp_seat == b'#').sum())
