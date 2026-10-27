# Array Implementation of Binary Trees

To avoid the cost of all the shifts in memory that we get from using Arrays, it is useful to implement Binary Trees with pointers from one element to the next, just like Binary Trees are implemented before this point, especially when the Binary Tree is modified often.

But in case we read from the Binary Tree a lot more than we modify it, an Array implementation of a Binary Tree can make sense as it needs less memory, it can be easier to implement, and it can be faster for certain operations due to cache locality.

> **Cache Locality** is when the fast cache memory in the computer stores parts of memory that was recently accessed, or when the cache stores parts of memory that is close to the address that is currently accessed. This happens because it is likely that the CPU needs something in the next cycle that is close to what it used in the previous cycle, either close in time or close in space.
>
> Since Array elements are stored contiguously in memory, one element right after the other, computers are sometimes faster when reading from Arrays because the next element is already cached, available for fast access in case the CPU needs it in the next cycle.

This Binary Tree can be stored in an Array starting with the root node R on index 0. The rest of the tree can be built by taking a node stored on index i, and storing its left child node on index 2⋅i+1, and its right child node on index 2⋅i+2.

Below is an Array implementation of the Binary Tree.

`binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']`

In this Array implementation, since the Binary Tree nodes are placed in an array, much of the code is about accessing nodes using indexes, and about how to find the correct indexes.

Let's say we want to find the left and right child nodes of node B. Because B is on index 2, B's left child is on index 2⋅2+1=5, which is node E, right? And B's right child is on index 2⋅2+2=6, which is node F, and that also fits with the drawing above, right?

As you can see on line 1, this implementation requires empty array elements where nodes have no child nodes. So to avoid wasting space on empty Array elements, Binary Trees stored using Array implementation should be a "perfect" Binary Tree, or a nearly perfect one.

A perfect Binary Tree is when every internal node have exactly two child nodes, and all leaf nodes are on the same level.

And the first line in the code above can be written without wasting space on empty Array elements:

`binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F']`

The list stores the tree by index: for a node at index i, its left child is at 2 _ i + 1 and its right child is at 2 _ i + 2. None represents an empty spot. The recursive functions use these formulas to walk the tree, returning an empty list when they reach an empty node or go past the end of the array.

The three functions differ in when they include the current node:

- Pre-order: current node, left subtree, right subtree.
- In-order: left subtree, current node, right subtree.
- Post-order: left subtree, right subtree, current node.

Each traversal starts at index 0, the root ('R').
