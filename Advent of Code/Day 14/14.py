robots = []
with open("Input.txt", "r") as file:
    for line in file:
        parts = line.split()
        p = list(map(int, parts[0].split('=')[1].split(',')))
        v = list(map(int, parts[1].split('=')[1].split(',')))
        robots.append([p, v])

rows, cols = 103, 101
m_r, m_c = rows // 2, cols // 2

# # Problem 1
final_positions = []
one, two, three, four = 0, 0, 0, 0
for robot in robots:
    p, v = robot
    p[0] += v[0] * 100
    p[1] += v[1] * 100
    f_pos = [p[0] % cols, p[1] % rows]
    final_positions.append(f_pos)
    x, y = f_pos
    if x < m_c and y < m_r:
        one += 1
    elif x > m_c and y < m_r:
        two += 1
    elif x < m_c and y > m_r:
        three += 1
    elif x > m_c and y > m_r:
        four += 1
# print(final_positions)
print(one, two, three, four)
print(one * two * three * four)

# Problem 2
import re

w, h = 101, 103
bots = [[*map(int, re.findall(r'-?\d+',l))]
                   for l in open('input.txt')]

def danger(t):
    a = b = c = d = 0

    for x, y, dx, dy in bots:
        x = (x + dx * t) % w
        y = (y + dy * t) % h

        a += x > w//2 and y > h//2
        b += x > w//2 and y < h//2
        c += x < w//2 and y > h//2
        d += x < w//2 and y < h//2

    return a * b * c * d

print(danger(100))
print(min(range(10_000), key=danger))