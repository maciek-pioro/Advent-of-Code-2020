# N4
# R90
# E1
# L90
# S5
# R90
# E4
# L180
# W1
# W2
# L90
# N1
# R90
# S5
# W4

f = open('input.txt', 'r')

rotToDir = {
    0: (1, 0),
    90: (0, 1),
    180: (-1, 0),
    270: (0, -1)
}

instrToDir: dict[str, tuple[int]] = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

rotSign = {
    'L': +1,
    'R': -1
}

x, y = 0, 0
rot = 0
dir = rotToDir[rot]
for l in f:
    instruction = l[0]
    arg = int(l[1:])
    dx, dy = 0, 0
    if instruction in ['N', 'E', 'S', 'W']:
        dx, dy = instrToDir[instruction]
    elif instruction in ['L', 'R']:
        rot = (rot + rotSign[instruction] * arg + 360) % 360
    elif instruction == 'F':
        dx, dy = rotToDir[rot]
    x += arg * dx
    y += arg * dy
print(x, y)