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
visited = set()

def traverse(i, j, infinite):
    # account for edge case where you have two hashtags at a turn
    direction = 'N'
    while i >= 0 and i < rows and j >= 0 and j < cols:
        visited.add((i, j))

        if (i, j, direction) in infinite:
            return True
        infinite.add((i, j, direction))

        new_i, new_j = i + directions[direction][0], j + directions[direction][1]
        if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols and grid[new_i][new_j] == "#":
            if direction == 'N':
                direction = 'E'
            elif direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
        else:
            i = new_i
            j = new_j
    return False

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '^':
            start = (i, j)
            break

# Problem 1
traverse(start[0], start[1], set())
print(len(visited))

# Problem 2
result2 = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '.':
            infinite = set()
            grid[i][j] = '#'
            if traverse(start[0], start[1], infinite):
                result2 += 1
            grid[i][j] = '.'
print(result2)
            
