"""
    Kruskal Algorithm for Minimum Spanning Tree (Disjoint Set)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

class DS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)

        if rootu != rootv:
            if self.rank[rootu] >= self.rank[rootv]:
                self.parent[rootv] = rootu
                self.rank[rootu] += 1
            else:
                self.parent[rootu] = rootv
                self.rank[rootv] += 1


class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.edges = []

    def add_edge(self, u, v, cost):
        self.edges.append((u, v, cost))

    def kruskal(self):
        mst = []
        ds = DS(self.num_vertices)

        self.edges.sort(key=lambda x: x[2])

        for edge in self.edges:
            u, v, cost = edge
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append(edge)

        return mst, ds.parent, ds.rank


g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 8)
g.add_edge(3, 4, 12)
mst, parent, rank = g.kruskal()
total_weight = sum(edge[2] for edge in mst)
print("Sorted Edges Based on Weight:")
for edge in sorted(g.edges, key=lambda x: x[2]):
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
print("\nMinimum Spanning Tree Edges:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
print("Total Weight of MST:", total_weight)
print("\nParent Matrix:")
print([i for i in range(g.num_vertices)])  # Print indices
print(parent)
print("\nRank Matrix:")
print(rank)
