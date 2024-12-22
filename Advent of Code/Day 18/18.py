from collections import deque

corrupt = []
directions = {
    'N': (-1, 0),    # North: move up (decrease y)
    'S': (1, 0),     # South: move down (increase y)
    'E': (0, 1),     # East: move right (increase x)
    'W': (0, -1),    # West: move left (decrease x)
}
with open("Input.txt", "r") as file:
    for line in file:
        corrupt.append(list(map(int, line.split(','))))

maximum = 71
n_corrupt = 1024

grid = [['.'] * maximum for i in range(maximum)]
for i in range(n_corrupt):
    x, y = corrupt[i][0], corrupt[i][1]
    grid[y][x] = '#'

# for row in grid: print(row)

# Problem 1
def bfs():
    result = float("inf")
    visited = set()
    q = deque([[(0, 0), 0]])
    while q:
        coords, score = q.popleft()
        i, j = coords
        if i == maximum-1 and j == maximum-1:
            result = min(score, result)

        for dx, dy in directions.values():
            nx, ny = i + dx, j + dy
            if 0 <= nx < maximum and 0 <= ny < maximum and grid[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), score+1))
    return result
# for i in range(1025, len(corrupt)):
#     x, y = corrupt[i][0], corrupt[i][1]
#     grid[y][x] = '#'
#     if bfs() == float('inf'):
#         print(i)
#         break
print(corrupt[3039])
