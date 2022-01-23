f = open('input.txt', 'r')
# f = open('toyInput.txt', 'r')

board = [l.strip() for l in f.readlines()]

x, y = 0, 0
dy, dx = 1, 3

height = len(board)
width = len(board[0])

trees = 0
while y<height:
    # print(y, x)
    if board[y][x] == '#':
        trees += 1
    y += dy
    x = (x+dx) % width
print(trees)