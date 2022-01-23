def conv(code: str):
    code = code.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(code, base=2)

f = open('input.txt', 'r')
seats = [(conv(l[0:7]), conv(l[7:10])) for l in f]
ind = [8*row + col for row, col in seats]
print(max(ind))