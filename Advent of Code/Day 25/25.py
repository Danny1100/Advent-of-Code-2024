locks, keys = [], []
with open("Input.txt") as file:
    current = []
    is_lock = None
    for line in file:
        if line == "\n":
            if is_lock:
                locks.append(current)
            else:
                keys.append(current)
            current = []
            is_lock = None
            continue

        if is_lock == None:
            if line.startswith("#"):
                is_lock = True
            elif line.startswith("."):
                is_lock = False

        current.append(list(line.strip()))

    if is_lock:
        locks.append(current)
    else:
        keys.append(current)


def print_items(items):
    for item in items:
        for row in item:
            print(row)
        print("\n")


# print("locks")
# print_items(locks)
# print("keys")
# print_items(keys)

# Problem 1
ln, kn = [], []
for lock in locks:
    rows, cols = len(lock), len(lock[0])
    current = []
    for j in range(cols):
        for i in range(rows - 1, -1, -1):
            if lock[i][j] == "#":
                current.append(i)
                break
    ln.append(current)

for key in keys:
    rows, cols = len(key), len(key[0])
    current = []
    for j in range(cols):
        for i in range(rows):
            if key[i][j] == "#":
                current.append(rows - 1 - i)
                break
    kn.append(current)

result = 0
for lock in ln:
    for key in kn:
        fits = True
        i = 0
        while i < len(key):
            l, k = lock[i], key[i]
            if l + k >= 6:
                fits = False
            i += 1
        if fits:
            result += 1

print(result)
