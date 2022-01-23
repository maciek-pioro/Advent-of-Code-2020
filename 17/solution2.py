import copy
from typing import List


def get_neighbors_number(x: int, y: int, z: int, w: int, cube) -> int:
    result: int = 0
    for d_x in [-1, 0, 1]:
        for d_y in [-1, 0, 1]:
            for d_z in [-1, 0, 1]:
                for d_w in [-1, 0, 1]:
                    if (d_x, d_y, d_z, d_w) == (0, 0, 0, 0):
                        continue
                    n_x = x + d_x
                    if n_x < 0 or n_x >= len(cube):
                        continue
                    n_y = y + d_y
                    if n_y < 0 or n_y >= len(cube[0]):
                        continue
                    n_z = z + d_z
                    if n_z < 0 or n_z >= len(cube[0][0]):
                        continue
                    n_w = w + d_w
                    if n_w < 0 or n_w >= len(cube[0][0][0]):
                        continue
                    if cube[n_x][n_y][n_z][n_w]:
                        result += 1
    return result


f = open('input.txt', 'r')
input = [l.strip() for l in f.readlines()]

ITERATION_NUMBER: int = 6

initial_board = [[c == '#' for c in row] for row in input]
# print(initial_board)

x_size, y_size, z_size, w_size = len(initial_board), len(initial_board[0]), 1, 1
max_x_size, max_y_size, max_z_size, max_w_size = x_size + 2 * ITERATION_NUMBER, y_size + \
    2 * ITERATION_NUMBER, z_size + 2 * ITERATION_NUMBER, w_size + 2 * ITERATION_NUMBER

prev_cube = [copy.deepcopy([copy.deepcopy([copy.deepcopy([False] * max_w_size)
                                           for _z in range(max_z_size)]) for _y in range(max_y_size)]) for _x in range(max_x_size)]
next_cube = copy.deepcopy(prev_cube)

for i in range(x_size):
    for j in range(y_size):
        prev_cube[ITERATION_NUMBER + i][ITERATION_NUMBER +
                                        j][ITERATION_NUMBER][ITERATION_NUMBER] = initial_board[i][j]

for _ in range(ITERATION_NUMBER):
    for x in range(max_x_size):
        for y in range(max_y_size):
            for z in range(max_z_size):
                for w in range(max_w_size):
                    neighbors = get_neighbors_number(x, y, z, w, prev_cube)
                    next_cube[x][y][z][w] = (prev_cube[x][y][z][w] and (neighbors == 2 or neighbors == 3)) or (
                        not prev_cube[x][y][z][w] and neighbors == 3)
    prev_cube, next_cube = next_cube, prev_cube

end_cube = prev_cube
result = 0
for x in range(max_x_size):
    for y in range(max_y_size):
        for z in range(max_z_size):
            for w in range(max_w_size):
                if end_cube[x][y][z][w]:
                    result += 1
print(result)
