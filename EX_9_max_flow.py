from collections import deque  # Import deque from collections for efficient queue operations

class MaxFlow:
    def __init__(self, graph):
        # Initialize the MaxFlow object with the original graph and create a residual graph.
        self.graph = graph  # Original graph
        self.residual_graph = [list(row) for row in graph]  # Create a residual graph (deep copy of original graph)
        self.size = len(graph)  # Number of vertices in the graph

    def bfs(self, source, sink, parent):
        # Perform a BFS to find if there is a path from source to sink in the residual graph.
        visited = [False] * self.size  # Track visited vertices
        queue = deque([source])  # Initialize queue with the source vertex
        visited[source] = True  # Mark source as visited

        while queue:
            u = queue.popleft()  # Dequeue a vertex from the queue

            for v, capacity in enumerate(self.residual_graph[u]):  # Iterate over adjacent vertices
                # If not yet visited and there is available capacity in the residual graph.
                if not visited[v] and capacity > 0:
                    queue.append(v)  # Enqueue the vertex
                    visited[v] = True  # Mark vertex as visited
                    parent[v] = u  # Record the path

                    # If we reached the sink, return True indicating a path is found.
                    if v == sink:
                        return True

        # No path found from source to sink.
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.size  # Array to store the path from source to sink.
        max_flow = 0  # Initialize max flow to 0.

        # Augment the flow while there is a path from source to sink.
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")  # Initialize path flow to infinity
            s = sink

            # Find the maximum flow through the path found by BFS.
            while s != source:
                path_flow = min(path_flow, self.residual_graph[parent[s]][s])  # Find minimum capacity in the path
                s = parent[s]

            v = sink

            # Update the residual capacities of the edges and reverse edges along the path.
            while v != source:
                u = parent[v]
                self.residual_graph[u][v] -= path_flow  # Subtract path flow from forward edge
                self.residual_graph[v][u] += path_flow  # Add path flow to reverse edge
                v = parent[v]

            # Add the path flow to the overall flow.
            max_flow += path_flow

        return max_flow  # Return the overall flow.

# Example usage:
graph = [
    [0, 16, 13, 0, 0, 0],  # Adjacency matrix representation of the graph
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]
source = 0  # Source vertex
sink = 5  # Sink vertex

# Create MaxFlow object and compute the maximum flow from source to sink.
max_flow_solver = MaxFlow(graph)  # Initialize MaxFlow with the given graph
max_flow = max_flow_solver.ford_fulkerson(source, sink)  # Compute the maximum flow
print(f"Maximum flow: {max_flow}")  # Output the maximum flow.
