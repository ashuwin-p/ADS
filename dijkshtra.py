"""
    Dijkshtra's Algorithm (Greedy Technique)
    -> Single source Shortest path Algorithm
    -> Works only with positive edge weights

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""


from my_graph import Graph
from tabulate import tabulate


def Dijkstra(graph, src):
    visited = []

    def all_visited():
        return len(visited) == len(graph._vertices)

    def min_cost_vertex(soln):
        result = None
        min_cost = float("inf")
        for vertex, data in soln.items():
            if (vertex not in visited) and (data[0] <= min_cost):
                min_cost = data[0]
                result = vertex
        return result

    solution = {vertex: [float("inf"), "None"] for vertex in graph._vertices}
    solution[src][0] = 0
    solution[src][1] = src

    vertex = src

    while not all_visited():
        vertex = min_cost_vertex(solution)

        visited.append(vertex)
        adjs = graph.adjacent(vertex)
        for adj in adjs:
            if adj not in visited:
                cost = solution[vertex][0] + graph.get_cost(vertex, adj)
                if cost < solution[adj][0]:
                    solution[adj][0] = cost
                    solution[adj][1] = vertex

        tabulate_solution(solution)

    return solution


def tabulate_solution(solution):
    table = []
    for vertex, data in solution.items():
        table.append([vertex, data[0], data[1]])
    result = tabulate(
        table, headers=["Vertex", "Shortest Distance", "Parent"], tablefmt="grid"
    )
    print(result)


if __name__ == "__main__":
    G = Graph()
    G.add_edge(1, 2, 2)
    G.add_edge(1, 3, 4)
    G.add_edge(2, 3, 1)
    G.add_edge(2, 4, 7)
    G.add_edge(3, 5, 3)
    G.add_edge(4, 6, 1)
    G.add_edge(5, 4, 2)
    G.add_edge(5, 6, 5)
    print("Graph : ", G)
    solution = Dijkstra(G, 1)
    print("\nSolution By Dijkstra")
    tabulate_solution(solution)
