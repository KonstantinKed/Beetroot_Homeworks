from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.v = vertex
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)

    def DFS(self, b, visited):
        visited[b] = True
        # visited.add(b)
        print(b, end=' ')
        for neighbour in self.graph[b]:
            if not visited[neighbour]:
                self.DFS(neighbour, visited)


    def fix_order(self, b, visited, stack): # similar to DFS but vertex is added to stack if visited
        visited[b] = True
        for neighbour in self.graph[b]:
            if not visited[neighbour]:
                self.fix_order(neighbour, visited, stack)
        stack = stack.append(b)

    def reverse_graph(self): # reverse graph to perform backward operation
        g = Graph(self.v)
        for neighbour in self.graph:
            for j in self.graph[neighbour]:
                g.addEdge(j, neighbour)
        return g

    def scc(self):
        stack = []
        visited = [False]*(self.v)
        for neighbour in range(self.v):
            if not visited[neighbour]:
                self.fix_order(neighbour, visited, stack)

        g_rev = self.reverse_graph()
        visited = [False] * (self.v)

        while stack:
            neighbour = stack.pop()
            if not visited[neighbour]:
                g_rev.DFS(neighbour, visited)
                print("")



g = Graph(8)

g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,0)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,4)
g.addEdge(6,7)

# g.DFS(0)
g.scc()
