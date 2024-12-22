grid = []
directions = [
    (-1, 0),    # North: move up (decrease y)
    (1, 0),     # South: move down (increase y)
    (0, 1),     # East: move right (increase x)
    (0, -1),    # West: move left (decrease x)
]
with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        grid.append(list(map(int, line)))
rows, cols = len(grid), len(grid[0])

# Problem 1
# result = 0

# def dfs(i, j, current):
#     if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] != current: return 0

#     visited.add((i, j))
#     if current == 9:
#         return 1
#     val = 0
#     for d in directions:
#         val += dfs(i + d[0], j + d[1], current + 1)
#     return val

# for i in range(rows):
#     for j in range(cols):
#         if grid[i][j] == 0:
#             visited = set()
#             result += dfs(i, j, 0)

# print(result)

# Problem 2
result = 0

def dfs(i, j, current):
    if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] != current: return 0

    visited.add((i, j))
    if current == 9:
        visited.remove((i, j))
        return 1
    val = 0
    for d in directions:
        val += dfs(i + d[0], j + d[1], current + 1)
    visited.remove((i, j))
    return val

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            visited = set()
            result += dfs(i, j, 0)

print(result)