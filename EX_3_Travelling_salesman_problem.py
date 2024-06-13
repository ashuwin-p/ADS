"""
    Travelling Salesman Problem Implementation
    (For Complete Graph)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 12 - 06- 2024
"""

from copy import deepcopy
from my_graph import Graph


class TSP:
    def __init__(self, graph):
        self.graph = graph
        self.optimal_cost = float("inf")
        self.optimal_path = None

    def getOptimalSoln(self, start):
        def dfs(self, vertex, visited, path, paths):
            visited.append(vertex)
            path.append(vertex)

            if len(visited) == len(self.graph._vertices):
                current_path = deepcopy(path)
                current_path.append(start)
                current_cost = self.graph.pathCost(current_path)
                if current_cost < self.optimal_cost:
                    self.optimal_cost, self.optimal_path = current_cost, current_path
                paths[tuple(current_path)] = current_cost

            for adj in self.graph.adjacent(vertex):
                if adj not in visited:
                    dfs(self, adj, visited, path, paths)

            visited.remove(vertex)  # backtracking
            path.pop()
            return paths

        all_details = dfs(self, start, [], [], {})
        print("Given Graph : ", self.graph._graph)
        print("\n\t Travelling Salesman Problem Solved \n\n")
        for path, cost in all_details.items():
            print(f"\t{path}   =>    {cost}")

        return (self.optimal_path, self.optimal_cost)


if __name__ == "__main__":

    def construct_graph():
        g = Graph()
        g.add_edge(1, 1, 0)
        g.add_edge(1, 2, 5)
        g.add_edge(1, 3, 1)
        g.add_edge(1, 4, 2)
        g.add_edge(2, 2, 0)
        g.add_edge(2, 3, 6)
        g.add_edge(2, 4, 10)
        g.add_edge(3, 3, 0)
        g.add_edge(3, 4, 5)
        g.add_edge(4, 4, 0)
        print(g.get_edges())
        return g

    graph = construct_graph()
    tsp = TSP(graph)
    optimal_path, optimal_cost = tsp.getOptimalSoln(1)
    print("\n\n Optimal Path : ", optimal_path)
    print("\n Optimal Cost : ", optimal_cost)
