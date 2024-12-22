grid = []
instructions = []
with open("Input.txt") as file:
    first_part = True
    for line in file:
        if line == '\n':
            first_part = False
        elif first_part:
            grid.append(list(line.strip()))
        elif not first_part:
            instructions += list(line.strip())

# for row in grid: print(row)
# print(instructions)

rows, cols = len(grid), len(grid[0])
mapping = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

# Problem 1
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            sx, sy = i, j
            break

def print_grid():
    for line in grid: print(line)
    print()

def move(grid, instructions):
    x, y = sx, sy
    for instruction in instructions:
        nx, ny = x + mapping[instruction][0], y + mapping[instruction][1]
        while grid[nx][ny] == 'O':
            nx += mapping[instruction][0]
            ny += mapping[instruction][1]
        # print(nx, ny, grid[nx][ny], instruction)
        if grid[nx][ny] == '#':
            continue
        elif grid[nx][ny] == '.':
            grid[x][y] = '.'
            grid[nx][ny] = 'O'
            x += mapping[instruction][0]
            y += mapping[instruction][1]
            grid[x][y] = '@'
        # print_grid()

    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                result += ((100*i) + j)
    return result
    
print(move(grid, instructions))