with open('input.txt', 'r') as reader:
    in_data = [(x[0], int(x[1:])) for x in reader.read().split('\n')]


class ship:
    def __init__(self):
        self.dir = 'E'
        self.east = 0
        self.north = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def clockwise(self, degrees):
        for i in range(0, degrees // 90):
            if self.waypoint_x >= 0 and self.waypoint_y >= 0: # первый квадрант
                self.waypoint_x, self.waypoint_y = abs(self.waypoint_y), -abs(self.waypoint_x)
            elif self.waypoint_x <= 0 and self.waypoint_y >= 0:  # второй квадрант
                self.waypoint_x, self.waypoint_y = abs(self.waypoint_y), abs(self.waypoint_x)
            elif self.waypoint_x <= 0 and self.waypoint_y <= 0:  # третий квадрант
                self.waypoint_x, self.waypoint_y = -abs(self.waypoint_y), abs(self.waypoint_x)
            else: # четвертый квадрант
                self.waypoint_x, self.waypoint_y = -abs(self.waypoint_y), -abs(self.waypoint_x)

    def contrclockwise(self, degrees):
        for i in range(0, degrees // 90):
            if self.waypoint_x >= 0 and self.waypoint_y >= 0:  # первый квадрант
                self.waypoint_x, self.waypoint_y = -abs(self.waypoint_y), abs(self.waypoint_x)
            elif self.waypoint_x <= 0 and self.waypoint_y >= 0:  # второй квадрант
                self.waypoint_x, self.waypoint_y = -abs(self.waypoint_y), -abs(self.waypoint_x)
            elif self.waypoint_x <= 0 and self.waypoint_y <= 0:  # третий квадрант
                self.waypoint_x, self.waypoint_y = abs(self.waypoint_y), -abs(self.waypoint_x)
            else:  # четвертый квадрант
                self.waypoint_x, self.waypoint_y = abs(self.waypoint_y), abs(self.waypoint_x)

    def move(self, direction, steps):
        if direction == 'N':
            self.waypoint_y += steps
        elif direction == 'S':
            self.waypoint_y -= steps
        elif direction == 'E':
            self.waypoint_x += steps
        elif direction == 'W':
            self.waypoint_x -= steps

    def move_forward(self, steps):
        for i in range(0, steps):
            self.north += self.waypoint_y
            self.east += self.waypoint_x

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

    print('n: {} e: {} w_x {} w_y {}'.format(my_ship.north, my_ship.east, my_ship.waypoint_x, my_ship.waypoint_y))

print(my_ship.manhattan())
