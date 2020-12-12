with open('input.txt', 'r') as reader:
    in_data = [(x[0], int(x[1:])) for x in reader.read().split('\n')]


class ship:
    def __init__(self):
        self.dir = 'E'
        self.east = 0
        self.north = 0

    def clockwise(self, degrees):
        for i in range(1, degrees // 90):
            if self.dir == 'W':
                self.dir = 'N'
            elif self.dir == 'N':
                self.dir = 'E'
            elif self.dir == 'E':
                self.dir = 'S'
            elif self.dir == 'S':
                self.dir = 'W'

    def contrclockwise(self, degrees):
        for i in range(1, degrees // 90):
            if self.dir == 'W':
                self.dir = 'S'
            elif self.dir == 'S':
                self.dir = 'E'
            elif self.dir == 'E':
                self.dir = 'N'
            elif self.dir == 'N':
                self.dir = 'W'

    def move(self, direction, steps):
        if direction == 'N':
            self.north += steps
        elif direction == 'S':
            self.north -= steps
        elif direction == 'E':
            self.east += steps
        elif direction == 'W':
            self.east -= steps

    def move_forward(self, steps):
        self.move(self.dir, steps)

    def manhattan(self):
        return abs(self.north) + abs(self.east)


my_ship = ship()

for command in in_data:
    if command[0] == 'L':
        my_ship.contrclockwise(command[1])
    elif command[0] == 'R':
        my_ship.clockwise(command[1])
    elif command[0] == 'F':
        my_ship.move_forward(command[1])
    else:
        my_ship.move(command[0], command[1])

print(my_ship.manhattan())
