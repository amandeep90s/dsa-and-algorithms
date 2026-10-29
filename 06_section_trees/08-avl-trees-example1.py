"""Insert values into an AVL tree and print them in sorted order.

An AVL tree is a binary search tree that keeps each node's left and right
subtrees within one level of each other by rotating unbalanced subtrees.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # A newly created node is a leaf, so its height is 1.
        self.height = 1

def getHeight(node):
    """Return a subtree's height; an empty subtree has height 0."""
    if not node:
        return 0
    return node.height

def getBalance(node):
    """Return left height minus right height for this node."""
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    print('Rotate right on node:', y.data)
    x = y.left
    # Keep x's right subtree so it can be reattached after the rotation.
    T2 = x.right

    # Move y below x; T2 becomes y's left subtree.
    x.right = y
    y.left = T2

    # Update the lower node first, then the new subtree root.
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    print('Rotate left on node',x.data)
    y = x.right
    # Keep y's left subtree so it can be reattached after the rotation.
    T2 = y.left

    # Move x below y; T2 becomes x's right subtree.
    y.left = x
    x.right = T2

    # Update the lower node first, then the new subtree root.
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    # Find the insertion point using the binary-search-tree ordering.
    if not node:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    # Equal values are not inserted, so this tree stores unique values.

    # Recompute this node's height after inserting into one of its subtrees.
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # A balance factor above 1 means the left subtree is too tall.
    # Left-Left case: the new value went into the left child's left subtree.
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left-Right case: first straighten the left child, then rotate this node.
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # A balance factor below -1 means the right subtree is too tall.
    # Right-Right case: the new value went into the right child's right subtree.
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right-Left case: first straighten the right child, then rotate this node.
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    # Return the (possibly unchanged) root of this subtree to the caller.
    return node

def inOrderTraversal(node):
    """Visit left subtree, node, then right subtree (sorted order)."""
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

# Insert each letter; insert may return a new root after a rotation.
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)

# In-order traversal prints the letters in ascending order.
inOrderTraversal(root)