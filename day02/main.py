with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]


def is_valid(cond_pass):
    cond, password = cond_pass.split(':')
    up_down, letter = cond.split(' ')
    down, up = up_down.split('-')

    valid = (password[int(down)] == letter and password[int(up)] != letter) or \
            (password[int(down)] != letter and password[int(up)] == letter)


    return valid


all_valid = [password for password in in_data if is_valid(password)]

print(len(all_valid))
