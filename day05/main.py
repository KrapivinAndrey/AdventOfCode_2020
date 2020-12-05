with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]


def get_seat(path: str) -> int:
    row = list(range(0, 128))
    column = list(range(0, 8))

    for dir in path:
        if dir == 'F':
            row = row[0:len(row) // 2]
        elif dir == 'B':
            row = row[len(row) // 2:]
        elif dir == 'L':
            column = column[0:len(column) // 2]
        elif dir == 'R':
            column = column[len(column) // 2:]

    return row[0] * 8 + column[0]


seats = set(range(0,862))
for x in in_data:
    seats.remove(get_seat(x))

print(seats)
