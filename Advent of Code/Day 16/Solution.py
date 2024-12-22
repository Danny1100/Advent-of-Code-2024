import sys
sys.setrecursionlimit(100000)

grid = []
directions = {
    'N': (-1, 0),    # North: move up (decrease y)
    'S': (1, 0),     # South: move down (increase y)
    'E': (0, 1),     # East: move right (increase x)
    'W': (0, -1),    # West: move left (decrease x)
}
with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        grid.append(line)
rows, cols = len(grid), len(grid[0])

# Problem 1
def dfs(i, j, direction, points):
    if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '#' or (i, j) in visited:
        return float('inf')
    if grid[i][j] == 'E':
        return points
    
    visited.add((i, j))
    res = float('inf')
    for d in directions:
        new_i, new_j = i + directions[d][0], j + directions[d][1]
        if d == direction:
            res = min(dfs(new_i, new_j, d, points+1), res)
        else:
            res = min(dfs(new_i, new_j, d, points+1001), res)
    visited.remove((i, j))
    return res

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            visited = set()
            result = dfs(i, j, 'E', 0)
            break
print(result)