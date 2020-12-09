import comp

with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]

for i in range(0, len(in_data)):

    new_data = in_data.copy()
    if new_data[i].find('nop') != -1:
        new_data[i] = new_data[i].replace('nop', 'jmp')
    elif new_data[i].find('jmp') != -1:
        new_data[i] = new_data[i].replace('jmp', 'nop')

    my_comp = comp.computer()
    my_comp.set_commands(new_data)
    try:
        my_comp.run()
    except IndexError:
        print('---')
        print(my_comp)
        break
    except Exception:
        continue
