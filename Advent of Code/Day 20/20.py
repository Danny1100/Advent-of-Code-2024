grid = []
directions = {
    "N": (-1, 0),  # North: move up (decrease y)
    "S": (1, 0),  # South: move down (increase y)
    "E": (0, 1),  # East: move right (increase x)
    "W": (0, -1),  # West: move left (decrease x)
}
with open("Input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))


def print_grid():
    for row in grid:
        print(row)


rows, cols = len(grid), len(grid[0])

si, sj = 0, 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            si, sj = i, j

path = [(si, sj)]
visited = set((si, sj))
x, y = si, sj
while grid[x][y] != "E":
    for direction, coords in directions.items():
        nx, ny = x + coords[0], y + coords[1]
        if (grid[nx][ny] == "." or grid[nx][ny] == "E") and (nx, ny) not in visited:
            x, y = nx, ny
            visited.add((nx, ny))
            path.append((nx, ny))
            break

# Problem 1 and 2
cache = {}
result = 0
for i in range(len(path)):
    for j in range(i + 2, len(path)):
        c1, c2 = path[i], path[j]
        distance = abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])
        if distance <= 20:
            saved = j - i - distance
            if saved not in cache:
                cache[saved] = 1
            else:
                cache[saved] += 1

            if saved >= 100:
                result += 1
# for key in sorted(cache.keys()):
#     print(key, cache[key])
print(result)
