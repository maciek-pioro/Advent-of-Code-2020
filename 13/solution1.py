f = open('input.txt', 'r')

earliest_timestamp = int(f.readline())
buses = [int(l) for l in f.readline().split(',') if l!='x']
print(buses)

timestamp = earliest_timestamp
while True:
    bus_found = False
    for bus in buses:
        if 0 == timestamp % bus:
            bus_found = True
            break
    if bus_found: break
    timestamp += 1
print((timestamp - earliest_timestamp) * bus)