class computer:
    def __init__(self):
        self.__pointer = 0
        self.__accumulator = 0
        self.__debug = False
        self.__commands = []
        self.history = [0]
        self.trace = [0]

    def __str__(self):
        return "point: {} accumulator: {}".format(self.__pointer, self.__accumulator)

    def __repr__(self):
        return str(self)

    def set_debug(self, state:bool):
        self.__debug = state

    def set_commands(self, commands):
        self.__commands = commands

    def __get_command(self):
        el = self.__commands[self.__pointer].split(' ')
        return el[0], int(el[1].replace('+', ''))

    def __check_deadloop(self):
        for i in range(1, len(self.trace) // 2 + 1):
            if self.trace[-i:] == self.trace[-2 * i:-i]:
                print(self.history[-i])
                raise Exception("Deadloop step back {}".format(len(self.trace) - i))

    def run(self):
        while True:

            print(self)

            command = self.__get_command()
            if command[0] == 'nop':
                self.__pointer += 1
            elif command[0] == 'acc':
                self.__accumulator += command[1]
                self.__pointer += 1
            elif command[0] == 'jmp':
                self.__pointer += command[1]

            self.trace.append(self.__pointer)
            self.history.append(self.__accumulator)
            self.__check_deadloop()








