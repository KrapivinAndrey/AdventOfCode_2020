with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n')]


def prepare_rules():
    res = {}
    for rule in in_data:
        left, right = rule.split('contain')
        color = left[:left.find('bags') - 1]
        res[color] = right

    return res


rules = prepare_rules()


def directly(type_of_bag:str)->set:
    res = set()

    for color, value in rules.items():

        if value.find(type_of_bag) > 0 and color not in res:
            res.add(color)

    return res


bags = directly('shiny gold')

repeat = True
while repeat:
    repeat = False
    temp = set()
    for bag in bags:
        for new_bag in directly(bag):
            if new_bag not in bags:
                temp.add(new_bag)
                repeat = True
    bags = set.union(bags, temp)

print(len(bags))

