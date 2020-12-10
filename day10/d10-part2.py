with open('input.txt', 'r') as reader:
    in_data = [int(x) for x in reader.read().split('\n')]

accumulator = {}

in_data.append(0)
last = max(in_data)+3
in_data.append(last)

accumulator[last] = 1

in_data.sort(reverse=True)

for i in range(1, len(in_data)):
    a = in_data[i]
    res = 0
    if a + 1 in in_data:
        res = res + accumulator[a + 1]
    if a + 2 in in_data:
        res = res + accumulator[a + 2]
    if a + 3 in in_data:
        res = res + accumulator[a + 3]

    accumulator[a] = res

print(accumulator[0])