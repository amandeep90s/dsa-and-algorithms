# Graphs Implementation

Before we can run algorithms on a Graph, we must first implement it somehow.

To implement a Graph we will use an Adjacency Matrix, like the one below.

To store data for each vertex, in this case the letters A, B, C, and D, the data is put in a separate array that matches the indexes in the adjacency matrix, like this:

`vertexData = [ 'A', 'B', 'C', 'D']`

For an undirected and not weighted Graph, like in the image above, an edge between vertices i and j is stored with value 1. It is stored as 1 on both places (j,i) and (i,j) because the edge goes in both directions. As you can see, the matrix becomes diagonally symmetric for such undirected Graphs.

Let's look at something more specific. In the adjacency matrix above, vertex A is on index 0, and vertex D is on index 3, so we get the edge between A and D stored as value 1 in position (0,3) and (3,0), because the edge goes in both directions.

## Graph Implementation Using Classes

A more proper way to store a Graph is to add an abstraction layer using classes so that a Graph's vertices, edges, and relevant methods, like algorithms that we will implement later, are contained in one place.

Programming languages with built-in object-oriented functionality like Python and Java, make implementation of Graphs using classes much easier than languages like C, without this built-in functionality.

## Implementation of Directed and Weighted Graphs

To implement a Graph that is directed and weighted, we just need to do a few changes to previous implementation of the undirected Graph.

To create directed Graphs, we just need to remove line 10 in the previous example code, so that the matrix is not automatically symmetric anymore.

The second change we need to do is to add a weight argument to the add_edge() method, so that instead of just having value 1 to indicate that there is an edge between two vertices, we use the actual weight value to define the edge.
