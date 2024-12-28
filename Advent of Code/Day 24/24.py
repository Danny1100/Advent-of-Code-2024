from collections import deque

cache = {}
gates = []
with open("Input.txt") as file:
    first_part = True
    for line in file:
        if line == "\n":
            first_part = False
            continue

        if first_part:
            key, val = line.strip().split(":")
            val = int(val)
            cache[key] = val
        else:
            v1, operand, v2, _, res = line.strip().split(" ")
            gates.append((v1, operand, v2, res))

# print(cache)
# print(gates)

# Problem 1
while gates:
    for gate in gates:
        k1, operand, k2, res = gate
        if k1 in cache and k2 in cache:
            v1, v2 = cache[k1], cache[k2]
            if operand == "AND":
                cache[res] = int(v1 and v2)
            elif operand == "OR":
                cache[res] = int(v1 or v2)
            elif operand == "XOR":
                cache[res] = int(v1 != v2)
            gates.remove(gate)

ls = []
for key, val in cache.items():
    if key.startswith("z"):
        ls.append((key, val))
ls.sort()

res = []
for _, n in ls:
    res.insert(0, str(n))
result = int("".join(res), 2)
print(result)

# Problem 2
x = []
for key, val in cache.items():
    if key.startswith("x"):
        x.append((key, val))
x.sort()
bin1 = []
for _, n in x:
    bin1.insert(0, str(n))
bin1 = "".join(bin1)

y = []
for key, val in cache.items():
    if key.startswith("y"):
        y.append((key, val))
y.sort()
bin2 = []
for _, n in y:
    bin2.insert(0, str(n))
bin2 = "".join(bin2)

int_sum = int(bin1, 2) + int(bin2, 2)
# Convert the sum back to binary and remove the '0b' prefix
expected = bin(int_sum)[2:]

print("expected: ", expected)
print(
    "actual: ",
    "".join(res),
)
int_diff = int("".join(res), 2) - int(expected, 2)
diff = bin(int_diff)[2:]
print("diff: ", diff)

ans = ["z14", "hbk", "z18", "kvn", "z23", "dbb", "tfn", "cvh"]
print(",".join(sorted(ans)))
