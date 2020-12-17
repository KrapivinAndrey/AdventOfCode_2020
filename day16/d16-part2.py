def parseRule(rule:str):
    name, other = rule.split(":")
    rules = [list(map(int, x.strip().split('-'))) for x in other.split('or')]

    return name, rules


def readRule(reader):
    result = {}
    r = reader.readline()
    while r != '\n':
        name, rules = parseRule(r)
        result[name] = rules
        r = reader.readline()

    return result


def readMyTicket(reader):
    reader.readline()  # Yout ticker
    return list(map(int, reader.readline().split(',')))


def readOtherTickets(reader):
    reader.readline()
    reader.readline()  # nearby tickets
    return [list(map(int, x.split(','))) for x in reader.readlines()]


def getInvalid(rules, ticket):
    result = []
    for num in ticket:
        invalid = 0
        for rule in rules.values():
            if not (rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]):
                invalid += 1
        if invalid == len(rules):
            result.append(num)
    return result


with open('input.txt', 'r') as reader:
    rules = readRule(reader)
    yourTicket = readMyTicket(reader)
    tickets = readOtherTickets(reader)

tickets = [ticket for ticket in tickets if getInvalid(rules, ticket) == []]
tickets.append(yourTicket)
orderRules = {}

for i in range(len(yourTicket)):
    for name, rule in rules.items():
        valid = True
        for ticket in tickets:
            num = ticket[i]
            if not (rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]):
                valid = False
                break
        if valid:
            orderRules.setdefault(i, []).append(name)

# Вычитка правил
res = 1
for i in range(len(yourTicket)):
    for order, rule in orderRules.items():
        if len(rule) == 1:
            break
    rule = rule[0]
    if rule.find('departure') != -1:
        res *= yourTicket[order]
    for otherRule in orderRules.values():
        if rule in otherRule:
            otherRule.remove(rule)

print(res)