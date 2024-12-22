data = []
with open("Input.txt", "r") as file:
    for line in file:
        data += list(map(int, list(line.strip())))

# Problem 1
# total_positions = 0
# for i in range(0, len(data), 2):
#     total_positions += data[i]

# result = 0
# position = 0
# i, j = 0, len(data)-1
# while position < total_positions:
#     if data[i] == 0:
#         i += 1
#         continue

#     if i % 2 == 0:
#         result += position * (i // 2)
#     else:
#         while data[j] == 0:
#             j -= 2
#         result += position * (j // 2)
#         data[j] -= 1
#     data[i] -= 1

#     position += 1
# print(result)

# Problem 2
files = []
ls = []
for i, c in enumerate(data):
    if i % 2 == 0:
        files.append(c)
        for j in range(c):
            ls.append(i // 2)
    else:
        for j in range(c):
            ls.append(-1)

back = len(files)-1
while back >= 0:
    for i, c in enumerate(ls):
        if c != -1: continue

        j, count = i, 0
        while j < len(ls) and ls[j] == -1:
            count += 1
            j += 1

        index = ls.index(back)
        if index < i: break

        n_files = files[back]
        if count >= n_files:
            for f in range(i, i + n_files):
                ls[f] = back
            for n in range(i+n_files, len(ls)):
                if ls[n] == back:
                    ls[n] = -1
            break
    # print(back, ls)
    print(back)
    back -= 1

result = 0
position = 0
for i, c in enumerate(ls):
    if c != -1:
        result += position * c
    position += 1
print(result)
