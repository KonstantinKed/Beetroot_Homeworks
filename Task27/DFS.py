from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)

    def DFS(self, b, visited=None):
        stack = []
        if visited is None:
            visited = set()
        visited.add(b)
        print(b, end=' ')
        for neighbour in self.graph[b]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)

    def reverse_graph(self): # reverse graph to perform backward operation
        g = Graph()
        for b in self.graph:
            for a in self.graph[b]:
                g.addEdge(a, b)
        return g


g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(2, 4)
g.DFS(0)
print('----')
gr = g.reverse_graph()
gr.DFS(4)
