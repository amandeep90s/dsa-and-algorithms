# Implementation of Depth First Search Traversal

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

    def dfs_util(self, startVertex, visited):
        # Mark the vertex before following its edges, so cycles cannot revisit it.
        visited[startVertex] = True
        print(self.vertexData[startVertex], end=' ')

        # Check every possible neighbor in index order.
        for i in range(self.size):
            if self.adjMatrix[startVertex][i] == 1 and not visited[i]:
                # Recursion explores this branch fully before returning to this loop.
                self.dfs_util(i, visited)

    def dfs(self, startVertexData):
        # Keep track of vertices already reached during this traversal.
        visited = [False] * self.size
        # Convert the requested label to the index used by the adjacency matrix.
        startVertex = self.vertexData.index(startVertexData)
        # Begin the recursive traversal at the selected vertex.
        self.dfs_util(startVertex, visited)


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

print("\nDepth First Search starting from vertex D:")
g.dfs('D')