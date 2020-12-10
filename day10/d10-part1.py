with open('input.txt', 'r') as reader:
    in_data = [int(x) for x in reader.read().split('\n')]

in_data.append(0)
in_data.append(max(in_data)+3)

in_data.sort()


def count_in_list(a:list, b:int)->int:
    res = 0
    for x in a:
        if x == b:
            res += 1

    return res

diff = [in_data[i+1] - in_data[i] for i in range(len(in_data)-1)]

print(count_in_list(diff, 1))
print(count_in_list(diff, 3))
