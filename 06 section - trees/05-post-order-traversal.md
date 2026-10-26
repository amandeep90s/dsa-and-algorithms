# Post Order Traversal

Post-order Traversal is a type of Depth First Search, where each node is visited in a certain order.

Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.

What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.

> Everyday example: Imagine cleaning a house by tidying the rooms to the living room's left and right first, then cleaning the living room last. This is post-order because you handle the main room after the other rooms.

The postOrderTraversal() function keeps traversing the left subtree recursively (line 4), until None is returned when C's left child node is called as the node argument.

After C's left child node returns None, line 5 runs and C's right child node returns None, and then the letter 'C' is printed (line 6).

This means that C is visited, or printed, "after" its left and right child nodes are traversed, that is why it is called "post" order traversal.

The postOrderTraversal() function continues to propagate back to previous recursive function calls, so the next node to be printed is 'D', then 'A'.

The function continues to propagate back and printing nodes until all nodes are printed, or visited.
