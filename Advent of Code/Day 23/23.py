import networkx as nx
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
new_cache = {}
for name, node in cache.items():
    new_cache[name] = set(map(lambda x: x.name, node.neighbors))
G = nx.Graph(new_cache)
maximal_cliques = list(
    nx.find_cliques(G)
)  # E.g. [['kh', 'ta'], ['kh', 'ub', 'qp'], ...]
largest_clique = max(maximal_cliques, key=len)  # E.g. ['ta', 'co', 'ka', 'de']
print(",".join(sorted(largest_clique)))
print(len(largest_clique))

# def dfs(current, subgraph, potential):
#     new_subgraph = copy.deepcopy(subgraph)
#     new_potential = copy.deepcopy(potential)
#     if current:
#         if current in new_subgraph:
#             return new_subgraph
#         new_potential.remove(current)
#         new_subgraph.add(current)
#         neighbor_names = set(map(lambda x: x.name, cache[current].neighbors))
#         new_potential = neighbor_names & potential

#         if len(potential) == 0:
#             return new_subgraph

#     result = new_subgraph
#     for node_name in new_potential:
#         res = dfs(node_name, new_subgraph, new_potential)
#         # print(res)

#         if len(res) > len(result):
#             result = res

#     return result


# visited = set()
# final_result = set()
# for name, node in cache.items():
#     if name in visited:
#         continue

#     subgraph = set({name})
#     potential = set()
#     for neighbor in node.neighbors:
#         potential.add(neighbor.name)
#     res = dfs(None, subgraph, potential)
#     for n in res:
#         visited.add(n)
#     print(name, res)
#     if len(res) > len(final_result):
#         final_result = res
# print(",".join(sorted(list(final_result))))


# def bron_kerbosch(R, P, X, graph):
#     if not P and not X:
#         yield R  # R is a maximal clique

#     while P:
#         # Pivoting: Choose a pivot with max neighbors in P
#         pivot = max(P | X, key=lambda u: len(graph[u] & P), default=None)

#         # Explore vertices not connected to the pivot
#         for v in P - graph[pivot]:
#             # Recursive call with v added to R
#             yield from bron_kerbosch(R | {v}, P & graph[v], X & graph[v], graph)

#             # Remove v from P and add to X (prune further)
#             P.remove(v)
#             X.add(v)


# def find_maximum_clique(graph):
#     cliques = list(bron_kerbosch(set(), set(graph), set(), graph))
#     return max(cliques, key=len)


# new_cache = {}
# for name, node in cache.items():
#     new_cache[name] = set(map(lambda x: x.name, node.neighbors))
# # print(new_cache)
# print(find_maximum_clique(new_cache))
