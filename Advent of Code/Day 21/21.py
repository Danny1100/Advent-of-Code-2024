from collections import deque

problems = []
numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
dpad = [
    ["#", "^", "A"],
    ["<", "v", ">"],
]
directions = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}
with open("Input.txt") as file:
    for line in file:
        problems.append(line.strip())


# Problem 1
# TODO: look at the answer. Notice that every start, end point on each keypad has a finite number of shortest paths.
# You need to find all of them and store in dict then go from there
