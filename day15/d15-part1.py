start = [1, 12, 0, 20, 8, 16]
been  = {}
for i in range(1, len(start) + 1):
    been[start[i-1]] = i
num = 0
for i in range(len(start) + 1, 30000001):
    print("Turn {}: num {}".format(i, num))
    prev = num
    if num not in been:
        num = 0
    else:
        num = i - been[num]
    been[prev] = i
