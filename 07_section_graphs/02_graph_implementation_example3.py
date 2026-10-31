# Graph Implementation Using Classes

class Graph:
    def __init__(self, size):
        self.adjMatrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertexData = [''] * size

    def addEdge(self, start, end):
        if 0 <= start < self.size and 0 <= end < self.size:
            self.adjMatrix[start][end] = 1
            self.adjMatrix[end][start] = 1  # For undirected graph

    def setVertexData(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertexData[vertex] = data

    def printGraph(self):
        print('\n Adjacency Matrix:')
        for row in self.adjMatrix:
            print(' '.join(map(str, row)))

        print("\n Vertex Data:")
        for vertex, data in enumerate(self.vertexData):
            print(f"{vertex}: {data}")

g = Graph(4)
g.setVertexData(0, 'A')
g.setVertexData(1, 'B')
g.setVertexData(2, 'C')
g.setVertexData(3, 'D')

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 2)

g.printGraph()
