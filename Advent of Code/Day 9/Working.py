from functools import reduce
blocks = []
m = n = 0
for i, c in enumerate(open("Input.txt").read()):
    s = int(c)
    if s:
        blocks.append([m, [] if i%2 else [(n, s)], s])
        if i%2<1: n+=1
        m += s
for block in [x for x in blocks[::-1] if len(x[1]) == 1]:
    file = block[1][0]
    if (space := next((y for y in blocks if y[0] < block[0] and y[2] - sum(z[1] for z in y[1]) >= file[1]), None)):
        space[1].append(file)
        block[1].clear()
print(sum(reduce(lambda i, f: (i[0]+f[0]*(f[1]*i[1]+f[1]*(f[1]-1)//2),i[1]+f[1]), B[1], (0, B[0]))[0] for B in blocks))

a = []
with open("Input.txt", "r") as file:
    for line in file:
        a += list(map(int, list(line.strip())))

sum = 0
block = 0
last = len(a)-1
# if last % 2 == 1: last -= 1
for i in range(len(a)):
    v=int(a[i])
    if i%2==0:
        for _ in (range(v)):
            sum+=((i//2)*block)
            block+=1
    else:
        for _ in range(v):
            while a[last] == 0:
                last-=2
            if last<=i:
                break
            sum+=((last//2)*block)
            block+=1
            a[last]-=1
print(sum)