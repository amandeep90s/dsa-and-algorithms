# AVL Trees

The AVL Tree is a type of Binary Search Tree named after two Soviet inventors Georgy Adelson-Velsky and Evgenii Landis who invented the AVL Tree in 1962.

AVL trees are self-balancing, which means that the tree height is kept to a minimum so that a very fast runtime is guaranteed for searching, inserting and deleting nodes, with time complexity O(logn).

The only difference between a regular Binary Search Tree and an AVL Tree is that AVL Trees do rotation operations in addition, to keep the tree balance.

A Binary Search Tree is in balance when the difference in height between left and right subtrees is less than 2.

By keeping balance, the AVL Tree ensures a minimum tree height, which means that search, insert, and delete operations can be done really fast.

The two trees above are both Binary Search Trees, they have the same nodes, and the same in-order traversal (alphabetical), but the height is very different because the AVL Tree has balanced itself.

Step through the building of an AVL Tree in the animation below to see how the balance factors are updated, and how rotation operations are done when required to restore the balance.

## Left and Right Rotations

To restore balance in an AVL Tree, left or right rotations are done, or a combination of left and right rotations.

The previous animation shows one specific left rotation, and one specific right rotation.

## The Balance Factor

A node's balance factor is the difference in subtree heights.

The subtree heights are stored at each node for all nodes in an AVL Tree, and the balance factor is calculated based on its subtree heights to check if the tree has become out of balance.

The height of a subtree is the number of edges between the root node of the subtree and the leaf node farthest down in that subtree.

The Balance Factor (BF) for a node (X) is the difference in height between its right and left subtrees.

BF(X) = height(right subtree of X) - height(left subtree of X)

Balance factor values

- 0: The node is in balance.
- more than 0: The node is "right heavy".
- less than 0: The node is "left heavy".

  If the balance factor is less than -1, or more than 1, for one or more nodes in the tree, the tree is considered not in balance, and a rotation operation is needed to restore balance.

## The Four "out-of-balance" Cases

When the balance factor of just one node is less than -1, or more than 1, the tree is regarded as out of balance, and a rotation is needed to restore balance.

There are four different ways an AVL Tree can be out of balance, and each of these cases require a different rotation operation.

| Case             | Description                                                                 | Rotation to Restore Balance                                                                        |
| ---------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Left-Left (LL)   | The unbalanced node and its left child node are both left-heavy.            | A single right rotation.                                                                           |
| Right-Right (RR) | The unbalanced node and its right child node are both right-heavy.          | A single left rotation.                                                                            |
| Left-Right (LR)  | The unbalanced node is left heavy, and its left child node is right heavy.  | First do a left rotation on the left child node, then do a right rotation on the unbalanced node.  |
| Right-Left (RL)  | The unbalanced node is right heavy, and its right child node is left heavy. | First do a right rotation on the right child node, then do a left rotation on the unbalanced node. |

## Time Complexity for AVL Trees

Take a look at the unbalanced Binary Search Tree below. Searching for "M" means that all nodes except 1 must be compared. But searching for "M" in the AVL Tree below only requires us to visit 4 nodes.

So in worst case, algorithms like search, insert, and delete must run through the whole height of the tree. This means that keeping the height (h) of the tree low, like we do using AVL Trees, gives us a lower runtime.

See the comparison of the time complexities between Binary Search Trees and AVL Trees below, and how the time complexities relate to the height (h) of the tree, and the number of nodes (n) in the tree.

- The BST is not self-balancing. This means that a BST can be very unbalanced, almost like a long chain, where the height is nearly the same as the number of nodes. This makes operations like searching, deleting and inserting nodes slow, with time complexity O(h)=O(n).
- The AVL Tree however is self-balancing. That means that the height of the tree is kept to a minimum so that operations like searching, deleting and inserting nodes are much faster, with time complexity O(h)=O(logn).

## O(logn) Explained

The fact that the time complexity is O(h)=O(logn) for search, insert, and delete on an AVL Tree with height h and nodes n can be explained like this:
