with open('input.txt', 'r') as reader:
    mark = int(reader.readline())
    buses = [x for x in reader.readline().split(',')]

def proc(busID:str)->int:
    if busID == 'x':
        return 1000000
    else:
        return (mark // int(busID) + 1)*int(busID) - mark


minID = min(buses, key=proc)
print(int(minID) * proc(minID))
