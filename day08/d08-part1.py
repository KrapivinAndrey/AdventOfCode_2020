import comp

with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]

my_comp = comp.computer()
my_comp.set_commands(in_data)
my_comp.run()
