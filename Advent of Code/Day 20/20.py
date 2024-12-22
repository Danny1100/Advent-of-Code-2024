from collections import deque

grid = []
directions = {
    'N': (-1, 0),    # North: move up (decrease y)
    'S': (1, 0),     # South: move down (increase y)
    'E': (0, 1),     # East: move right (increase x)
    'W': (0, -1),    # West: move left (decrease x)
}
with open("Input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

for row in grid: print(row)
rows, cols = len(grid), len(grid[0])

# Problem 1
def bfs(si, sj):
    result = float("inf")
    visited = set((si, sj))
    q = deque([[(si, sj), 0]])
    while q:
        coords, score = q.popleft()
        i, j = coords
        if grid[i][j] == 'E':
            return score

        for dx, dy in directions.values():
            nx, ny = i + dx, j + dy
            if grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append([(nx, ny), score+1])

    return result

si, sj = 0, 0
original = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            si, sj = i, j
            original = bfs(si, sj)
            print(original)

result = 0
for i in range(rows):
    for j in range(cols):
        if i != 0 and i != rows-1 and j != 0 and j != rows-1 and grid[i][j] == '#':
            grid[i][j] = '.'
            res = bfs(si, sj)
            if original - res >= 100:
                result += 1
            grid[i][j] = '#'
print(result)