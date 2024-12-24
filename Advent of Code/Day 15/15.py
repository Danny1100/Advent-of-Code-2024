from collections import deque

grid = []
instructions = []
with open("Input.txt") as file:
    first_part = True
    for line in file:
        if line == "\n":
            first_part = False
        elif first_part:
            row = []
            for char in list(line.strip()):
                if char == "#":
                    row.append("#")
                    row.append("#")
                elif char == "O":
                    row.append("[")
                    row.append("]")
                elif char == ".":
                    row.append(".")
                    row.append(".")
                else:
                    row.append("@")
                    row.append(".")
            grid.append(row)
        elif not first_part:
            instructions += list(line.strip())


def print_grid():
    for line in grid:
        print(line)
    print()


print_grid()
# print(instructions)

rows, cols = len(grid), len(grid[0])
mapping = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

# Problem 2
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "@":
            sx, sy = i, j
            break


def move(grid, instructions):
    x, y = sx, sy
    for instruction in instructions:
        nx, ny = x + mapping[instruction][0], y + mapping[instruction][1]
        if grid[nx][ny] == "#":
            # print(instruction)
            # print_grid()
            continue
        elif grid[nx][ny] == ".":
            grid[nx][ny] = "@"
            grid[x][y] = "."
            x, y = nx, ny
            # print(instruction)
            # print_grid()
            continue

        can_shift = True
        # shift boxes up or down
        if instruction == "^" or instruction == "v":
            q = deque([(nx, ny, grid[nx][ny])])
            visited = set()
            visited.add((nx, ny))
            while q:
                qx, qy, symbol = q.popleft()
                if symbol == "[" and (qx, qy + 1) not in visited:
                    visited.add((qx, qy + 1))
                    q.append((qx, qy + 1, grid[qx][qy + 1]))
                elif symbol == "]" and (qx, qy - 1) not in visited:
                    visited.add((qx, qy - 1))
                    q.append((qx, qy - 1, grid[qx][qy - 1]))
                nqx, nqy = qx + mapping[instruction][0], qy + mapping[instruction][1]
                if grid[nqx][nqy] == "#":
                    can_shift = False
                    break
                elif (nqx, nqy) not in visited and (
                    grid[nqx][nqy] == "[" or grid[nqx][nqy] == "]"
                ):
                    visited.add((nqx, nqy))
                    q.append((nqx, nqy, grid[nqx][nqy]))

            if can_shift:
                descend = instruction == "v"
                sorted_list = sorted(list(visited), reverse=descend)
                for x_coord, y_coord in sorted_list:
                    if descend:
                        grid[x_coord + 1][y_coord] = grid[x_coord][y_coord]
                        grid[x_coord][y_coord] = "."
                    else:
                        grid[x_coord - 1][y_coord] = grid[x_coord][y_coord]
                        grid[x_coord][y_coord] = "."
                grid[nx][ny] = "@"
                grid[x][y] = "."
                x, y = nx, ny

        # shift boxes left or right
        else:
            while grid[nx][ny] == "[" or grid[nx][ny] == "]":
                nx += mapping[instruction][0]
                ny += mapping[instruction][1]
            if grid[nx][ny] == "#":
                can_shift = False

            if can_shift:
                while nx != x or ny != y:
                    ox, oy = nx - mapping[instruction][0], ny - mapping[instruction][1]
                    grid[nx][ny] = grid[ox][oy]
                    grid[ox][oy] = "."
                    nx, ny = ox, oy
                x += mapping[instruction][0]
                y += mapping[instruction][1]

        # print(instruction)
        # print_grid()

    print_grid()
    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "[":
                top = i
                left = j
                res = (top * 100) + left
                result += res
                print(i, j, res)

    return result


print(move(grid, instructions))
