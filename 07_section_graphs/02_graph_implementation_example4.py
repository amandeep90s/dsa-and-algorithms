# Implementation of Directed and Weighted Graphs

class Graph:
    def __init__(self, size):
        self.adjMatrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertexData = [''] * size

    def addEdge(self, start, end, weight):
        if 0 <= start < self.size and 0 <= end < self.size:
            self.adjMatrix[start][end] = weight

    def setVertexData(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertexData[vertex] = data

    def printGraph(self):
        print('\n Adjacency Matrix:')
        for row in self.adjMatrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))

        print("\n Vertex Data:")
        for vertex, data in enumerate(self.vertexData):
            print(f"{vertex}: {data}")

g = Graph(4)
g.setVertexData(0, 'A')
g.setVertexData(1, 'B')
g.setVertexData(2, 'C')
g.setVertexData(3, 'D')

g.addEdge(0, 1, 3)  # A -> B with weight 3
g.addEdge(0, 2, 2)  # A -> C with weight 2
g.addEdge(3, 0, 4)  # D -> A with weight 4
g.addEdge(2, 1, 1)  # C -> B with weight 1

g.printGraph()
