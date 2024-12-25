import heapq
import copy

grid = []
directions = {
    "N": (-1, 0),  # North: move up (decrease y)
    "S": (1, 0),  # South: move down (increase y)
    "E": (0, 1),  # East: move right (increase x)
    "W": (0, -1),  # West: move left (decrease x)
}
with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        grid.append(line)
rows, cols = len(grid), len(grid[0])


def print_grid():
    for row in grid:
        print(row)


for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            sx, sy = i, j


# Problem 1
def djikstras(sx, sy):
    result = set()
    shortest = float("inf")
    visited = set()
    pq = []
    heapq.heappush(pq, (0, [(sx, sy)], sx, sy, "E"))
    while pq:
        distance, path, x, y, direction = heapq.heappop(pq)
        visited.add((x, y, direction))

        if distance > shortest:
            break

        if grid[x][y] == "E":
            shortest = distance
            # print(path)
            # print(pq)
            for p in path:
                result.add(p)

        for d_name, d_vals in directions.items():
            nx, ny = x + d_vals[0], y + d_vals[1]
            if (
                nx >= 0
                and nx < rows
                and ny >= 0
                and ny < cols
                and (nx, ny, d_name) not in visited
                and grid[nx][ny] != "#"
            ):
                new_path = copy.deepcopy(path)
                new_path.append((nx, ny))
                if d_name == direction:
                    heapq.heappush(pq, (distance + 1, new_path, nx, ny, d_name))
                else:
                    heapq.heappush(pq, (distance + 1001, new_path, nx, ny, d_name))
    return result


result = djikstras(sx, sy)
# print(result)
print(len(result))
# for x, y in result:
#     grid[x][y] = "O"

# print_grid()
