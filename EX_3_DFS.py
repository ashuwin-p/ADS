"""
    Graph DFS Implementation

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from my_graph import Graph
from copy import deepcopy


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        if len(self._stack) >= 1:
            val = self._stack.pop(-1)
            return val
        else:
            raise IndexError("Stack is Empty")

    def isEmpty(self):
        return len(self._stack) == 0


def DFS(graph, src, target, request=None):
    """1 >> Simple Single DFS path with given start vertex to target vertex"""

    def __dfs_1(vertex, target, path, visit):
        visit.append(vertex)
        path.append(vertex)

        if vertex == target:
            return path

        for vtx in graph.adjacent(vertex):
            if vtx not in visit:
                result = __dfs_1(vtx, target, path, visit)
                if result is not None:
                    return result

        path.pop()  # backtrack
        return None

    """ 2 >> All DFS paths with given start vertex"""

    def __dfs_2(vertex, target, visit, path, paths):
        visit.append(vertex)
        path.append(vertex)

        if vertex == target:
            dfs = deepcopy(path)
            paths.append(dfs)

        for vtx in graph.adjacent(vertex):
            if vtx not in visit:
                __dfs_2(vtx, target, visit, path, paths)

        visit.remove(vertex)
        path.pop()  # backtrack

        return paths

    """3 >> DFS implementation using Stack"""

    def __dfs_3(src, target):
        stack = Stack()
        stack.push(src)
        visited = [src]
        path = []
        while not (stack.isEmpty()):
            vertex = stack.pop()
            path.append(vertex)

            if vertex == target:
                return path

            for adj in graph.adjacent(vertex):
                if adj not in visited:
                    visited.append(adj)
                    stack.push(adj)
        return None

    if request is None or (request == 1):
        return __dfs_1(src, target, [], [])

    elif request == 2:
        return __dfs_2(src, target, [], [], [])

    elif request == 3:
        return __dfs_3(src, target)


if __name__ == "__main__":
    G = Graph()
    G.add_edge(1, 2, 12)
    G.add_edge(2, 3, 34)
    G.add_edge(2, 5, 15)
    G.add_edge(5, 3, 30)
    G.add_edge(3, 4, 24)
    G.add_edge(4, 1, 14)
    G.add_edge(3, 1, 16)
    print("1 >> Simple Single DFS path with given start vertex to target vertex")
    print("2 >> All DFS paths with given start vertex")
    print("3 >> DFS implementation using Stack")
    choice = int(input("Enter the Choice : "))
    ans = DFS(G, 1, 4, choice)
    print(ans)
