import re

blocks = []
with open("Input.txt", "r") as file:
    lines = file.read().splitlines()
    block = { 'A': [], 'B': [], 'Prize': []}
    for line in lines:
        if line.startswith('Button A'):
            numbers = re.findall(r'X\+(\d+), Y\+(\d+)', line)
            x, y = map(int, numbers[0])
            block['A'] = [x, y]
        elif line.startswith('Button B'):
            numbers = re.findall(r'X\+(\d+), Y\+(\d+)', line)
            x, y = map(int, numbers[0])
            block['B'] = [x, y]
        elif line.startswith('Prize'):
            numbers = re.findall(r'X\=(\d+), Y\=(\d+)', line)
            x, y = map(int, numbers[0])
            block['Prize'] = [x, y]
            blocks.append(block)
            block = { 'A': [], 'B': [], 'Prize': []}

# Problem 1
def dp(i, j, current_tokens, a_press, b_press):
    if (i, j) in cache: return cache[(i, j)]
    if i == block['Prize'][0] and j == block['Prize'][1]:
        return current_tokens
    if i > block['Prize'][0] or j > block['Prize'][1] or a_press > 100 or b_press > 100:
        return float("inf")
    
    ax, ay, bx, by = block['A'][0], block['A'][1], block['B'][0], block['B'][1]
    cache[(i, j)] = min(dp(i+bx, j+by, current_tokens+1, a_press, b_press+1), dp(i+ax, j+ay, current_tokens+3, a_press+1, b_press))
    return cache[(i, j)]

result = 0
for block in blocks:
    cache = {}
    res = dp(0, 0, 0, 0, 0)
    if res != float("inf"):
        result += res
print(result)
