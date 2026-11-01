# Implementation of Breadth First Search Traversal

class Graph:
    def __init__(self, size):
        # A 1 means two vertices are connected; 0 means there is no edge.
        self.adjMatrix = [[0] * size for _ in range(size)]
        self.size = size
        # Store a readable label for each vertex index.
        self.vertexData = [''] * size

    def addEdge(self, start, end):
        if 0 <= start < self.size and 0 <= end < self.size:
            # Set both directions because this example uses an undirected graph.
            self.adjMatrix[start][end] = 1
            self.adjMatrix[end][start] = 1

    def setVertexData(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertexData[vertex] = data

    def printGraph(self):
        print("\n Adjacency matrix:")
        for row in self.adjMatrix:
            print(' '.join(map(str, row)))
        print("\n Vertex data:")
        for vertex, data in enumerate(self.vertexData):
            print(f"Vertex {vertex}: {data}")

    def bfs(self, startVertexData):
        queue = [self.vertexData.index(startVertexData)]
        visited = [False] * self.size
        visited[queue[0]] = True

        while queue:
            currentVertex = queue.pop(0)
            print(self.vertexData[currentVertex], end=' ')

            for i in range(self.size):
                if self.adjMatrix[currentVertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph(7)

g.setVertexData(0, 'A')
g.setVertexData(1, 'B')
g.setVertexData(2, 'C')
g.setVertexData(3, 'D')
g.setVertexData(4, 'E')
g.setVertexData(5, 'F')
g.setVertexData(6, 'G')

g.addEdge(3, 0)  # D - A
g.addEdge(0, 2)  # A - C
g.addEdge(0, 3)  # A - D
g.addEdge(0, 4)  # A - E
g.addEdge(4, 2)  # E - C
g.addEdge(2, 5)  # C - F
g.addEdge(2, 1)  # C - B
g.addEdge(2, 6)  # C - G
g.addEdge(1, 5)  # B - F

g.printGraph()

print("\nBreadth First Search starting from vertex D:")
g.bfs('D')