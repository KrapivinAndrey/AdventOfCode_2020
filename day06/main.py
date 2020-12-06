with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n\n')]


def count_answer_yes(declaration:str)->int:

    check = {}
    for group in declaration.split('\n'):
        for answer in group:
            check[answer] = 1

    return len(check)


res = 0
for x in in_data:
    res+=count_answer_yes(x)

print(res)