with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n\n')]


def count_answer_yes(declaration:str)->int:

    check = {}
    size_of_group = 0
    for group in declaration.split('\n'):
        size_of_group += 1
        for answer in group:
            if answer not in check:
                check[answer] = 1
            else:
                check[answer] += 1

    return len([x for x in check.values() if x == size_of_group])


res = 0
for x in in_data:
    res += count_answer_yes(x)
print(res)
