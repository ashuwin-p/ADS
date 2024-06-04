class Graph:
    def __init__(self):
        self._graph = {}
        self._vertices = []

    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._graph[vertex] = {}

    def add_edge(self, src, dest, cost):
        if src not in self._vertices:
            self.add_vertex(src)
        if dest not in self._vertices:
            self.add_vertex(dest)
        self._graph[src][dest] = cost

        # for undirected graph activate the below line
        # self._graph[dest][src] = cost

    def get_cost(self, src, dest):
        try:
            return self._graph[src][dest]
        except:
            # If edge not found
            return False
        
    def get_edges(self):
        edges = []
        for src in self._graph:
            for dest in self._graph[src]:
                edges.append((src, dest, self._graph[src][dest]))
        return edges

    def adjacent(self, vertex):
        return (self._graph[vertex]).keys()
    
    def __str__(self):
        return str(self._graph)
