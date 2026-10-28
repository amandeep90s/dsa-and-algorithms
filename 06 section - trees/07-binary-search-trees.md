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

## Insert a Node in a BST

Inserting a node in a BST is similar to searching for a value. All nodes in the BST are unique, so in case we find the same value as the one we want to insert, we do nothing.

> How it works:
>
> 1. Start at the root node.
> 2. Compare each node:
>
> - Is the value lower? Go left.
> - Is the value higher? Go right.
>
> 3. Continue to compare nodes with the new value until there is no right or left to compare with. That is where the new node is inserted.

## Find The Lowest Value in a BST Subtree

The next section will explain how we can delete a node in a BST, but to do that we need a function that finds the lowest value in a node's subtree.

> How it works:
>
> 1. Start at the root node of the subtree.
> 2. Go left as far as possible.
> 3. The node you end up in is the node with the lowest value in that BST subtree.

## Delete a Node in a BST

To delete a node, our function must first search the BST to find it.

After the node is found there are three different cases where deleting a node must be done differently.

How it works:

1. If the node is a leaf node, remove it by removing the link to it.
2. If the node only has one child node, connect the parent node of the node you want to remove to that child node.
3. If the node has both right and left child nodes: Find the node's in-order successor, change values with that node, then delete it.

In step 3 above, the successor we find will always be a leaf node, and because it is the node that comes right after the node we want to delete, we can swap values with it and delete it.

Node 8 is a leaf node (case 1), so after we find it, we can just delete it.

Node 19 has only one child node (case 2). To delete node 19, the parent node 15 is connected directly to node 18, and then node 19 can be removed.

Node 13 has two child nodes (case 3). We find the successor, the node that comes right after during in-order traversal, by finding the lowest node in node 13's right subtree, which is node 14. Value 14 is put into node 13, and then we can delete node 14.

## BST Balance and Time Complexity

On a Binary Search Tree, operations like inserting a new node, deleting a node, or searching for a node are actually O(h). That means that the higher the tree is (h), the longer the operation will take.

The reason why we wrote that searching for a value is O(logn) in the table above is because that is true if the tree is "balanced".

We call this tree balanced because there are approximately the same number of nodes on the left and right side of the tree.

The exact way to tell that a Binary Tree is balanced is that the height of the left and right subtrees of any node only differs by one. In the image above, the left subtree of the root node has height h=2, and the right subtree has height h=3.

For a balanced BST, with a large number of nodes (big n), we get height h≈log2n, and therefore the time complexity for searching, deleting, or inserting a node can be written as O(h)=O(logn).

But, in case the BST is completely unbalanced, like in the image below, the height of the tree is approximately the same as the number of nodes, h≈n, and we get time complexity O(h)=O(n) for searching, deleting, or inserting a node.
