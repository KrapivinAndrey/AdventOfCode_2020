with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]


def is_valid(cond_pass):
    cond, password = cond_pass.split(':')
    up_down, letter = cond.split(' ')
    down, up = up_down.split('-')

    valid = int(down) <= password.count(letter) <= int(up)

    return valid


valid = [password for password in in_data if is_valid(password)]

print(len(valid))
