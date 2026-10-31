# A Basic Graph Implementation

vertexData = ['A', 'B', 'C', 'D']

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

print('vertexData:',vertexData)
printAdjacencyMatrix(adjacencyMatrix)