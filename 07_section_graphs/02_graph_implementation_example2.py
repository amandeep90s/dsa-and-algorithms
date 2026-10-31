# A Basic Graph Implementation

vertexData = ['A', 'B', 'C', 'D']

# Rows and columns use the same order as vertexData; 1 means an edge connects
# the corresponding vertices. This undirected graph has a symmetric matrix.
adjacencyMatrix = [
    [0, 1, 1, 1], # Edges for vertex A
    [1, 0, 1, 0], # Edges for vertex B
    [1, 1, 0, 0], # Edges for vertex C
    [1, 0, 0, 0]  # Edges for vertex D
]

def printAdjacencyMatrix(matrix):
    print('\n Adjacency Matrix:')
    for row in matrix:
        print(row)

def printConnections(matrix, vertices):
    print("\n Connections for each vertex:")
    # Each row lists one vertex's connections; matching columns identify neighbors.
    for i in range(len(vertices)):
        print(f"{vertices[i]}:", end="")
        for j in range(len(vertices)):
            if matrix[i][j]: # If there is a connection
                print(vertices[j], end=" ")
        print() # new line after each vertex's connections

print('vertexData:',vertexData)
printAdjacencyMatrix(adjacencyMatrix)
printConnections(adjacencyMatrix, vertexData)