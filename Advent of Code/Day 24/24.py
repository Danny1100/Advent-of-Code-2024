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
