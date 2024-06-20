"""
    Cycle Detection in Directed Graph using DFS & Backtracking

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 20 - 06- 2024
"""

from my_graph import Graph


class Cycle_Check:
    def __init__(self):
        self.graph = None

    def dfs_check(self, node, visited, pathVisited):
        # Mark the current node as visited and part of the current path
        visited[node] = True
        pathVisited[node] = True

        # Iterate through all adjacent nodes
        for adj in self.graph.adjacent(node):
            if not visited[adj]:
                # If the adjacent node has not been visited, recursively call dfs_check
                if self.dfs_check(adj, visited, pathVisited):
                    return True
            elif pathVisited[adj]:
                # If the adjacent node is in the current path, a cycle is detected
                return True

        # Backtrack: mark the current node as not part of the current path
        pathVisited[node] = False
        return False

    def has_cycle(self, graph):
        self.graph = graph
        vertices = self.graph._vertices
        visited = {vertex: False for vertex in vertices}
        pathVisited = {vertex: False for vertex in vertices}

        for vertex in vertices:
            if not visited[vertex]:
                if self.dfs_check(vertex, visited, pathVisited):
                    print("Cycle Found!")
                    return True
        print("No Cycle Found!")
        return False


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2, 10)
    g.add_edge(2, 3, 20)
    g.add_edge(3, 1, 15)  # Uncomment this line to add a cycle

    check = Cycle_Check()
    check.has_cycle(g)
