# Problem 1
grid = []
directions = {
    'N': (-1, 0),    # North: move up (decrease y)
    'S': (1, 0),     # South: move down (increase y)
    'E': (0, 1),     # East: move right (increase x)
    'W': (0, -1),    # West: move left (decrease x)
    'NE': (-1, 1),   # North-East: move up and right (decrease y, increase x)
    'NW': (-1, -1),  # North-West: move up and left (decrease y, decrease x)
    'SE': (1, 1),    # South-East: move down and right (increase y, increase x)
    'SW': (1, -1)    # South-West: move down and left (increase y, decrease x)
}
letters = ['X', 'M', 'A', 'S']
with open("Input.txt", "r") as file:
    for line in file:
        char_list = list(line.strip())
        grid.append(char_list)

result = [0]
rows, cols = len(grid), len(grid[0])
def dfs(i, j, dir, letter_index):
    if i < 0 or j < 0 or i >= rows or j >= cols: return

    current_letter = letters[letter_index]
    if current_letter != grid[i][j]: return
    if letter_index == len(letters) - 1:
        result[0] += 1
        return
    
    direction = directions[dir]
    dfs(i + direction[0], j + direction[1], dir, letter_index + 1)
    

for i in range(rows):
    for j in range(cols):
        for dir in directions:
            dfs(i, j, dir, 0)
print(result)

# Problem 2
def check_xmas(l1, l2):
    if l1 == 'M' and l2 == 'S' or l1 == 'S' and l2 == 'M': return True
    return False

result2 = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'A':
            i1, i2 = i-1, i+1
            j1, j2 = j-1, j+1
            if i1 < 0 or j1 < 0 or i1 >= rows or j1 >= cols: continue
            if i2 < 0 or j2 < 0 or i2 >= rows or j2 >= cols: continue
            if check_xmas(grid[i-1][j-1], grid[i+1][j+1]) and check_xmas(grid[i-1][j+1], grid[i+1][j-1]):
                result2 += 1
print(result2)
