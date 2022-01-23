def getOccupiedAround(board, x, y):
    occupied = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0: continue
            neigh_x = x + i
            neigh_y = y + j
            if board[neigh_y][neigh_x] == '#':
                occupied += 1
    return occupied

def getOccupied(board):
    result = 0
    for row in board:
        for el in row:
            if el == '#':
                result += 1
    return result

def splitString(s: str) -> list[str]:
    return [c for c in s]

f = open('input.txt', 'r')

board = [['.'] + splitString(l.strip()) + ['.'] for l in f]
board.insert(0, '.' * len(board[0]))
board.append('.' * len(board[0]))

changed = True
while(changed):
    new_board = [l[:] for l in board]
    changed = False
    for y, row in enumerate(board):
        for x, el in enumerate(row):
            # print(el)
            if el == '.': continue
            occupiedAround = getOccupiedAround(board, x, y)
            if el == '#' and occupiedAround >= 4:
                new_board[y][x] = 'L'        
                changed = True
            if el == 'L' and occupiedAround == 0:
                new_board[y][x] = '#'
                changed = True
    board = new_board

print(getOccupied(board))