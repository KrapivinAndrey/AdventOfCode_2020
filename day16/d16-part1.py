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


with open('input.txt', 'r') as reader:
    rules = readRule(reader)
    yourTicket = readMyTicket(reader)
    tickets = readOtherTickets(reader)


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


errorRate = 0
for ticket in tickets:
    errorRate += sum(getInvalid(rules, ticket))

print(errorRate)