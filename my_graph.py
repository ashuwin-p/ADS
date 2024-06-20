"""
    Graph Implementation

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

class Graph:
    def __init__(self):
        self._graph = {}
        self._vertices = []
        self._edges = []

    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._graph[vertex] = {}

    def add_edge(self, src, dest, cost):
        if src not in self._vertices:
            self.add_vertex(src)
        if dest not in self._vertices:
            self.add_vertex(dest)

        self._graph[src][dest] = cost
        edge = (src, dest, cost)
        self._edges.append(edge)

        # for undirected graph activate the below line
        self._graph[dest][src] = cost

    def get_cost(self, src, dest):
        try:
            return self._graph[src][dest]
        except:
            # If edge not found
            return False
        
    def get_edges(self):
        return self._edges

    def adjacent(self, vertex):
        return list(self._graph[vertex].keys())
    
    def cost(self, src, dest):
        return self._graph[src][dest]

    def pathCost(self, path):
        pathcost = 0
        n = len(path)
        for i in range(n - 1):
            pathcost += self.cost(path[i], path[i + 1])
        return pathcost
    
    def __str__(self):
        return str(self._graph)
