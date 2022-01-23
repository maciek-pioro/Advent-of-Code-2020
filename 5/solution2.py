def conv(code: str):
    code = code.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(code, base=2)

f = open('input.txt', 'r')
seats = [(conv(l[0:7]), conv(l[7:10])) for l in f]
ind = [8*row + col for row, col in seats]
M = max(ind)
free = (M+1)*[True]
for i in ind:
    free[i] = False
for i in range(1, len(free)-1):
    if not free[i-1] and not free[i+1] and free[i]:
        print(i)
        exit()
