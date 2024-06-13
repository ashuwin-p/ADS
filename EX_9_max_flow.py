class Graph:
    def __init__(self, graph):
        self.graph = graph  # Initialize the graph with the given adjacency matrix
        self.ROW = len(graph)  # Number of rows in the adjacency matrix

    def BFS(self, s, t, parent):
        """
        Run Breadth-First Search (BFS) algorithm to find a path from source to sink
        in the residual graph.
        """
        visited = [False] * (self.ROW)  # Initialize all vertices as not visited
        queue = []  # Initialize a queue for BFS

        queue.append(s)  # Enqueue the source vertex
        visited[s] = True  # Mark the source vertex as visited

        while queue:
            u = queue.pop(0)  # Dequeue a vertex from the queue

            for ind, val in enumerate(self.graph[u]):
                # Check if the vertex is not visited and there is a residual capacity
                if visited[ind] == False and val > 0:
                    queue.append(ind)  # Enqueue the vertex
                    visited[ind] = True  # Mark the vertex as visited
                    parent[ind] = u  # Set the parent of the vertex
                    if ind == t:  # If we reach the sink, return True
                        return True

        return False  # If no path found from source to sink, return False

    def FordFulkerson(self, source, sink):
        """
        Implement the Ford-Fulkerson algorithm to find maximum flow in the given graph.
        """
        parent = [-1] * (self.ROW)  # Initialize parent array to track the augmenting path

        max_flow = 0  # Initialize the maximum flow to zero
        while self.BFS(source, sink, parent):  # While there is a path from source to sink
            path_flow = float("Inf")  # Initialize path flow to infinity
            s = sink  # Set the sink as the current vertex
            while s != source:  # Traverse the path from sink to source
                path_flow = min(path_flow, self.graph[parent[s]][s])  # Update path flow
                s = parent[s]  # Move to the parent vertex

            max_flow += path_flow  # Add path flow to maximum flow

            v = sink  # Set the sink as the current vertex
            while v != source:  # Traverse the path from sink to source
                u = parent[v]  # Get the parent of the current vertex
                self.graph[u][v] -= path_flow  # Update residual capacities
                self.graph[v][u] += path_flow  # Update residual capacities for reverse edge
                v = parent[v]  # Move to the parent vertex
        
        # Printing the path from source to sink
        for i in parent:
            print(i, "->", end="")
        print()

        return max_flow  # Return the maximum flow

# Create a graph given in the above diagram
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

g = Graph(graph)
source = 0
sink = 5
print("The maximum possible flow is %d" % g.FordFulkerson(source, sink))
