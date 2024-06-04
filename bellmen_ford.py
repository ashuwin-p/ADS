"""
    Bellmen Ford Algorithm (Dynamic Programming)
    -> Single Source Shortest path Algorithm
    -> Works with Negative edge weights
    -> Detects Negative Cycle in Graph
    -> Principle : Edge relaxation ( n-1 times )

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2401 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from my_graph import Graph


class Bellmen_Ford:
    def __init__(self, graph):
        self.__graph = graph

    def single_source_shortest_path(self, src):
        vertices = self.__graph._vertices
        edges = self.__graph.get_edges()
        # distance - Memoization dictionary [stores current shortest distance]
        distance = {vertex: float("inf") for vertex in vertices}
        distance[src] = 0
        n = len(vertices)
        update = True
        for _ in range(n - 1):
            if update is False:
                break

            update = False
            for edge in edges:
                src, dest, cost = edge
                if distance[src] + cost < distance[dest]:
                    distance[dest] = distance[src] + cost
                    update = True
        return distance


if __name__ == "__main__":
    G = Graph()
    G.add_edge(1, 2, 6)
    G.add_edge(1, 3, 5)
    G.add_edge(1, 4, 5)
    G.add_edge(2, 5, -1)
    G.add_edge(6, 7, 3)
    G.add_edge(5, 7, 2)
    G.add_edge(4, 6, -1)
    G.add_edge(3, 2, -2)
    G.add_edge(3, 5, 1)
    G.add_edge(4, 3, -2)

    B = Bellmen_Ford(G)
    print(B.single_source_shortest_path(1))
