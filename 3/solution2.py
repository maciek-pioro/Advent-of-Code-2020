f = open('input.txt', 'r')

board = [l.strip() for l in f.readlines()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

height = len(board)
width = len(board[0])

trees = 1
for slope in slopes:
    x, y = 0, 0
    (dx, dy) = slope
    slopetrees = 0
    while y<height:
        if board[y][x] == '#':
            slopetrees += 1
        y += dy
        x = (x+dx) % width
    trees *= slopetrees
print(trees)