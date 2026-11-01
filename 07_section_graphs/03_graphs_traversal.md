# Graphs Traversal

To traverse a Graph means to start in one vertex, and go along the edges to visit other vertices until all vertices, or as many as possible, have been visited.

Understanding how a Graph can be traversed is important for understanding how algorithms that run on Graphs work.

The two most common ways a Graph can be traversed are:

- Depth First Search (DFS)
- Breadth First Search (BFS)

DFS is usually implemented using a Stack or by the use of recursion (which utilizes the call stack), while BFS is usually implemented using a Queue.

> The **Call Stack** keeps functions running in the correct order.
>
> If for example FunctionA calls FunctionB, FunctionB is placed on top of the call stack and starts running. Once FunctionB is finished, it is removed from the stack, and then FunctionA resumes its work.

## Depth First Search Traversal

Depth First Search is said to go "deep" because it visits a vertex, then an adjacent vertex, and then that vertex' adjacent vertex, and so on, and in this way the distance from the starting vertex increases for each recursive iteration.

How it works:

- Start DFS traversal on a vertex.
- Do a recursive DFS traversal on each of the adjacent vertices as long as they are not already visited.
