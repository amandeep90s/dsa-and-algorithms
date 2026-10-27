# Binary Search Trees

A **Binary Search Tree** is a Binary Tree where every node's left child has a lower value, and every node's right child has a higher value.

A clear advantage with Binary Search Trees is that operations like search, delete, and insert are fast and done without having to shift values in memory.

A Binary Search Tree (BST) is a type of Binary Tree data structure, where the following properties must be true for any node "X" in the tree:

The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.

- The right child, and all its descendants have higher values than X's value.
- Left and right subtrees must also be Binary Search Trees.
- These properties makes it faster to search, add and delete values than a regular binary tree.

To make this as easy to understand and implement as possible, let's also assume that all values in a Binary Search Tree are unique.

The **size** of a tree is the number of nodes in it (n).

A **subtree** starts with one of the nodes in the tree as a local root, and consists of that node and all its descendants.

The **descendants** of a node are all the child nodes of that node, and all their child nodes, and so on. Just start with a node, and the descendants will be all nodes that are connected below that node.

The **node's height** is the maximum number of edges between that node and a leaf node.

A **node's in-order successor** is the node that comes after it if we were to do in-order traversal. In-order traversal of the BST above would result in node 13 coming before node 14, and so the successor of node 13 is node 14.

## Traversal of a Binary Search Tree

Just to confirm that we actually have a Binary Search Tree data structure in front of us, we can check if the properties at the top of this page are true. So for every node in the figure above, check if all the values to the left of the node are lower, and that all values to the right are higher.

Another way to check if a Binary Tree is BST, is to do an in-order traversal (like we did on the previous page) and check if the resulting list of values are in an increasing order.

As we can see by running the code example above, the in-order traversal produces a list of numbers in an increasing (ascending) order, which means that this Binary Tree is a Binary Search Tree.

## Search for a Value in a BST

Searching for a value in a BST is very similar to how we found a value using Binary Search on an array.

For Binary Search to work, the array must be sorted already, and searching for a value in an array can then be done really fast.

Similarly, searching for a value in a BST can also be done really fast because of how the nodes are placed.

> How it works:
>
> 1. Start at the root node.
> 2. If this is the value we are looking for, return.
> 3. If the value we are looking for is higher, continue searching in the right subtree.
> 4. If the value we are looking for is lower, continue searching in the left subtree.
> 5. If the subtree we want to search does not exist, depending on the programming language, return None, or NULL, or something similar, to indicate that the value is not inside the BST.

The time complexity for searching a BST for a value is O(h), where h is the height of the tree.

For a BST with most nodes on the right side for example, the height of the tree becomes larger than it needs to be, and the worst case search will take longer. Such trees are called unbalanced.
