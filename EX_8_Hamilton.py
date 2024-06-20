"""
    Hamilton Circuits using DFS & Backtracking

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 20 - 06- 2024
"""

from my_graph import Graph
from copy import deepcopy

def get_Hamilton_Circuits(graph, start):
    def dfs(graph, current_vertex, visited, current_path, all_paths):
        visited.append(current_vertex)
        current_path.append(current_vertex)

        # Check if all vertices are visited and there is an edge back to the start
        if len(current_path) == len(graph.vertices):
            if graph.get_cost(current_vertex, start) is not None:
                circuit = deepcopy(current_path)
                circuit.append(start)
                all_paths.append(circuit)
        
        # Explore adjacent vertices
        for neighbour in graph.adjacent(current_vertex):
            if neighbour not in visited:
                dfs(graph, neighbour, visited, current_path, all_paths)
        
        # Backtrack: remove the current vertex from path and visited list
        visited.remove(current_vertex)
        current_path.pop()

        return all_paths

    # Start DFS from the start vertex
    return dfs(graph, start, [], [], [])

g = Graph()
g.add_edge(1,2,10)
g.add_edge(2,3,10)
g.add_edge(2,4,10)
g.add_edge(4,3,10)
g.add_edge(4,1,10)
g.add_edge(3,1,10)
g.add_edge(3,4,10)

print(get_Hamilton_Circuits(g, 1))