grid = []
with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        grid.append(line)
rows, cols = len(grid), len(grid[0])

cache = {}
for i in range(rows):
    for j in range(cols):
        symbol = grid[i][j]
        if symbol == '.': continue
        if symbol not in cache:
            cache[symbol] = []
        cache[symbol].append((i, j))

def valid_coords(x, y):
    if x >= 0 and y >= 0 and x < rows and y < cols:
        return True
    return False

# Problem 1
antinodes = set()
for symbol in cache.keys():
    values = cache[symbol]
    for i in range(len(values)):
        x1, y1 = values[i]
        for j in range(i+1, len(values)):
            x2, y2 = values[j]

            dx1, dy1 = x1-x2 + x1, y1-y2 + y1
            if valid_coords(dx1, dy1):
                antinodes.add((dx1, dy1))
            dx2, dy2 = x2-x1 + x2, y2-y1 + y2
            if valid_coords(dx2, dy2):
                antinodes.add((dx2, dy2))
print(len(antinodes))

# Problem 2
antinodes2 = set()
for symbol in cache.keys():
    values = cache[symbol]
    for i in range(len(values)):
        x1, y1 = values[i]
        for j in range(i+1, len(values)):
            x2, y2 = values[j]

            orig_dx1, orig_dy1 = x1-x2, y1-y2
            dx1, dy1 = orig_dx1, orig_dy1
            while valid_coords(dx1 + x1, dy1 + y1):
                antinodes2.add((dx1 + x1, dy1 + y1))
                dx1 = dx1 + orig_dx1
                dy1 = dy1 + orig_dy1

            orig_dx2, orig_dy2 = x2-x1, y2-y1
            dx2, dy2 = orig_dx2, orig_dy2
            while valid_coords(dx2 + x2, dy2 + y2):
                antinodes2.add((dx2 + x2, dy2 + y2))
                dx2 = dx2 + orig_dx2
                dy2 = dy2 + orig_dy2
for i in range(rows):
    for j in range(cols):
        if grid[i][j] != '.' and (i, j) not in antinodes2:
            antinodes2.add((i, j))
print(len(antinodes2))
