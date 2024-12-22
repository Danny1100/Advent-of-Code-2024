grid = []
finished = set() # checks if a region has already been counted
directions = [
    (-1, 0),    # North: move up (decrease y)
    (1, 0),     # South: move down (increase y)
    (0, 1),     # East: move right (increase x)
    (0, -1),    # West: move left (decrease x)
]

with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        grid.append(line)
rows, cols = len(grid), len(grid[0])

# Problem 1
# returns tuple: (area, perimeter)
def dfs(i, j, letter):
    if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != letter:
        return [0, 1, True]
    if (i, j) in visited:
        return [0, 0, False]
    
    visited.add((i, j))
    finished.add((i, j))

    res = [1, 0, False]
    for d in directions:
        area, perimeter, edge = dfs(i + d[0], j + d[1], letter)
        if edge:
            cache[d].add((i, j))
        res[0] += area
        res[1] += perimeter
    return res

result = 0
result2 = 0
for i in range(rows):
    for j in range(cols):
        if (i, j) in finished: continue
        visited = set()
        cache = {
            (-1, 0): set(),
            (1, 0): set(),
            (0, -1): set(),
            (0, 1): set()
        }
        area, perimeter, edge = dfs(i, j, grid[i][j])
        result += area * perimeter

        sides = 0
        # print(grid[i][j], cache)
        for d in cache.keys():
            s = 1
            edges = list(cache[d])
            if d == (-1, 0) or d == (1, 0):
                edges = sorted(edges, key=lambda x: (x[0], x[1]))
                for k in range(1, len(edges)):
                    if edges[k][0] != edges[k-1][0] or edges[k][1] != edges[k-1][1] + 1:
                        # if d == (-1, 0) and grid[i][j] == 'A':
                        #     print(edges[k], edges[k-1], edges)
                        s += 1
            else:
                edges = sorted(edges, key=lambda x: (x[1], x[0]))
                for k in range(1, len(edges)):
                    if edges[k][1] != edges[k-1][1] or edges[k][0] != edges[k-1][0] + 1:
                        s += 1
            sides += s
            # print(grid[i][j], d, s)
        result2 += area * sides
print(result)
print(result2)