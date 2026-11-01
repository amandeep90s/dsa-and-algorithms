# Graphs Cycle Detection

A cycle in a Graph is a path that starts and ends at the same vertex, where no edges are repeated. It is similar to walking through a maze and ending up exactly where you started.

A cycle can be defined slightly different depending on the situation. A self-loop for example, where an edge goes from and to the same vertex, might or might not be considered a cycle, depending on the problem you are trying to solve.

## Cycle Detection

It is important to be able to detect cycles in Graphs because cycles can indicate problems or special conditions in many applications like networking, scheduling, and circuit design.

The two most common ways to detect cycles are:

- Depth First Search (DFS): DFS traversal explores the Graph and marks vertices as visited. A cycle is detected when the current vertex has an adjacent vertex that has already been visited.
- Union-Find: This works by initially defining each vertex as a group, or a subset. Then these groups are joined for every edge. Whenever a new edge is explored, a cycle is detected if two vertices already belong to the same group.

## DFS Cycle Detection for Undirected Graphs

To detect cycles in an undirected Graph using Depth First Search (DFS), we use a code very similar to the DFS traversal code on the previous page, with just a few changes.

How it works:

1. Start DFS traversal on each unvisited vertex (in case the Graph is not connected).
2. During DFS, mark vertices as visited, and run DFS on the adjacent vertices (recursively).
3. If an adjacent vertex is already visited and is not the parent of the current vertex, a cycle is detected, and True is returned.
4. If DFS traversal is done on all vertices and no cycles are detected, False is returned.
