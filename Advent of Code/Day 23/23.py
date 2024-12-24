from collections import deque


class Node:
    def __init__(self, name, neighbors=None):
        self.name = name
        self.neighbors = neighbors if neighbors is not None else []


cache = {}
with open("Input.txt") as file:
    for line in file:
        nodes = line.strip().split("-")
        name1, name2 = nodes[0], nodes[1]
        node1 = Node(name1) if name1 not in cache else cache[name1]
        node2 = Node(name2) if name2 not in cache else cache[name2]
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        if name1 not in cache:
            cache[name1] = node1
        if name2 not in cache:
            cache[name2] = node2

# for name, node in cache.items():
#     print(name)
#     for n in node.neighbors:
#         print(n.name)
#     print()


# Problem 1
# cache2 = {}
# calculated = set()  # set of already calculated names
# result = 0
# for name, node in cache.items():
#     if name.startswith("t") and name not in calculated:
#         calculated.add(name)

#         cache2[name] = 0

#         visited = set()  # set of already visited nodes
#         visited.add(node)
#         q = deque([(node, 0)])
#         while q:
#             cnode, distance = q.popleft()
#             for neighbor in cnode.neighbors:
#                 if distance == 2 and neighbor.name == name:
#                     # print(name, cnode.name)
#                     cache2[name] += 1
#                     result += 1
#                 if (
#                     distance < 2
#                     and neighbor.name not in calculated
#                     and neighbor not in visited
#                 ):
#                     q.append((neighbor, distance + 1))
# print(result // 2)
# print(cache2)


# Problem 2
def dfs(node, visited, potential):
    # returns the greatest size fully connected graph including this node
    if node in visited or len(potential) == 0:
        return 0

    visited.add(node)
    potential.add(node)

    for neighbor in node.neighbors:
        potential.add(neighbor)

    for neighbor in node.neighbors:
        dfs(neighbor)

    return


result = 0
for name, node in cache.items():
    res = dfs(node, set(), set())
    result = max(res, result)
    print(res)
print()
print(result)
