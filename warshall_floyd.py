"""
    Warshall Floyd Algorithm (Dynamic Programming)
    -> All pair Shortest path Algorithm

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2401 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from my_graph import Graph
from tabulate import tabulate


def Walshall_Floyd(graph):
    # memoization dicionary - prev_distance
    prev_distance = graph._graph
    vertices = graph._vertices
    for k in vertices:
        distance = {vertex: {} for vertex in vertices}
        for i in vertices:
            for j in vertices:
                if (i == j) or (i == k) or (j == k):
                    # No change in distance
                    distance[i][j] = prev_distance[i][j]
                else:
                    distance[i][j] = min(
                        prev_distance[i][j], prev_distance[i][k] + prev_distance[k][j]
                    )
        prev_distance = distance
        display(distance)

    solution = prev_distance

    return solution


def display(solution):
    vertices = list(solution.keys())
    table = []

    # Create header row
    header = ["Vertices"] + vertices
    table.append(header)

    # Create rows for each vertex
    for vertex in vertices:
        row = [vertex] + [solution[vertex][v] for v in vertices]
        table.append(row)
    print()
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    G = Graph()
    G.add_edge("A", "C", 3)
    G.add_edge("B", "A", 2)
    G.add_edge("D", "A", 6)
    G.add_edge("C", "D", 1)
    G.add_edge("C", "B", 7)
    # set all remaining distances to infinity
    for src in G._vertices:
        for dest in G._vertices:
            try:
                G._graph[src][dest]
            except:
                if src == dest:
                    G.add_edge(src, dest, 0)
                else:
                    G.add_edge(src, dest, float("inf"))
    print(f"\n solution : {Walshall_Floyd(G)}")
