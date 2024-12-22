problems = []
numpad = [[7, 8, 9], [4, 5, 6], [1, 2, 3], ["#", 0, "A"]]
dpad = [
    ["#", "^", "A"],
    ["<", "v", ">"],
]
with open("Input.txt") as file:
    for line in file:
        problems.append(list(line.strip()))


# Problem 1
def get_index(symbol, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return (i, j)
    return None


def get_distance(symbol, grid, current_layer):
    x, y = get_index(symbol, grid)
    ax, ay = get_index("A", grid)
    dx, dy = abs(x - ax), abs()
