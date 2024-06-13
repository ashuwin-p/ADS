"""
    Graph BFS Implementation

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""


from my_graph import Graph

class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, val):
        self._queue.append(val)

    def dequeue(self):
        if not self.isEmpty():
            val = self._queue.pop(0)
            return val
        else:
            raise IndexError("Queue is Empty")

    def isEmpty(self):
        return len(self._queue) == 0
    


def BFS(graph, src, target):
    Q = Queue()
    bfs = []
    visited = []
    Q.enqueue(src)
    visited.append(src)

    while not(Q.isEmpty()):
        vertex = Q.dequeue()
        bfs.append(vertex)
        if vertex == target:
            return bfs
        
        for adj in graph.adjacent(vertex):
            if adj not in visited:
                visited.append(adj)
                Q.enqueue(adj)
    
    return None

if __name__ == "__main__":
    G = Graph()
    G.add_edge(1, 2, 12)
    G.add_edge(2, 3, 34)
    G.add_edge(2, 5, 15)
    G.add_edge(5, 3, 30)
    G.add_edge(3, 4, 24)
    print(BFS(G, 1, 4))