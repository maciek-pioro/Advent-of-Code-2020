f = open('input.txt', 'r')

f.readline()
buses: list[tuple[int, int]] = [(int(num), i) for i, num in enumerate(f.readline().split(',')) if num!='x']
x, _ = buses[0]
product = x
for n, r in buses[1:]:
    while 0 != (x + r)%n:
        x += product
    product *= n
print(x)
