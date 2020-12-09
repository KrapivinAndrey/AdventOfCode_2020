with open('input.txt', 'r') as reader:
    in_data = [int(x) for x in reader.read().split('\n')]

preambula = 25

for i in range(preambula+1, len(in_data)):
    flag = False
    for a in range(1, preambula):
        for b in range(a + 1, preambula + 1):
            if in_data[i] == in_data[i - a] + in_data[i - b]:
                flag = True
                break
        if flag:
            break
    if not flag:
        print(in_data[i])
        break
