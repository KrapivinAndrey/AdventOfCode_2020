with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]


def prepare_rules():
    res = {}
    for rule in in_data:
        left, right = [x.strip() for x in rule.split('contain')]
        color = left[:left.find('bags')].strip()
        res[color] = contain(right)

    return res


def contain(task:str):
    import re
    pattern = '(\d+) ([\w+\s]+) bag[s]?'

    if task == "no other bags.":
        res = []
    else:
        res = re.findall(pattern, task)

    return res


rules = prepare_rules()


def how_many_contain(bag: str) ->int:

    res = 0
    for in_bag in rules[bag]:
        res += int(in_bag[0]) + int(in_bag[0]) * how_many_contain(in_bag[1])

    return res

print(how_many_contain('shiny gold'))

