with open('input.txt', 'r') as reader:
    in_data = [int(x) for x in reader.read().split('\n')]

weakness = 41682220

for i in range(0, len(in_data)):
    checksum = 0
    k = i
    while checksum < weakness:
        checksum += in_data[k]
        k += 1
    if checksum == weakness:
        right_set = in_data[i:k]
        break

print(min(right_set) + max(right_set))