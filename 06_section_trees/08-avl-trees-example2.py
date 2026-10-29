"""Insert into and delete from an AVL tree, then print its values in order.

An AVL tree is a binary search tree that uses rotations to keep its height
balanced after insertions and deletions.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # A leaf node has height 1; an empty subtree has height 0.
        self.height = 1

def getHeight(node):
    """Return a node's height, treating an empty subtree as height 0."""
    if not node:
        return 0
    return node.height

def getBalance(node):
    """Return left subtree height minus right subtree height."""
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    x = y.left
    # Save the subtree that will move from x's right to y's left.
    T2 = x.right

    # Rotate x above y while preserving the binary-search-tree ordering.
    x.right = y
    y.left = T2

    # Recalculate heights from the lower node up to the new subtree root.
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    y = x.right
    # Save the subtree that will move from y's left to x's right.
    T2 = y.left

    # Rotate y above x while preserving the binary-search-tree ordering.
    y.left = x
    x.right = T2

    # Recalculate heights from the lower node up to the new subtree root.
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
    # Equal values are ignored, so the tree contains unique values.

    # Update height and balance after inserting into a child subtree.
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Left-Left: the left subtree is heavy and its left side is at least as
    # tall as its right side, so one right rotation restores balance.
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left-Right: rotate the left child left, then rotate this node right.
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right-Right: one left rotation restores balance.
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right-Left: rotate the right child right, then rotate this node left.
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    # Return this subtree's root (which may have changed after a rotation).
    return node

def inOrderTraversal(node):
    """Print the values in ascending order using left-node-right traversal."""
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)
    
def minValueNode(node):
    """Find the smallest value in a subtree by following left children."""
    current = node
    while current.left is not None:
        current = current.left
    return current

def minValueNode(node):
    """Find the smallest value in a subtree by following left children."""
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    """Remove data from this subtree and rebalance it if necessary."""
    # If the subtree is empty, the value was not found.
    if not node:
        return node

    # Search for the value as in an ordinary binary search tree.
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # With no left child, replace this node with its right child.
        if node.left is None:
            temp = node.right
            node = None
            return temp
        # With no right child, replace this node with its left child.
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # With two children, copy the in-order successor (smallest value in
        # the right subtree), then remove its original node from that subtree.
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    # A deletion may have emptied this subtree, so there is no height to update.
    if node is None:
        return node

    # Recompute height and balance while the recursive call unwinds.
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Left-heavy, with the left child also left-heavy or balanced: right rotate.
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left-heavy, but the left child leans right: left-right double rotation.
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right-heavy, with the right child also right-heavy or balanced: left rotate.
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right-heavy, but the right child leans left: right-left double rotation.
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    # Return the root so callers reconnect the possibly rotated subtree.
    return node

# Build the initial AVL tree; insertion may change the root after rotations.
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)

# In-order traversal displays the current tree in sorted order.
inOrderTraversal(root)
print('\nDeleting A')
# Keep the root returned by delete in case rebalancing rotates the tree.
root = delete(root,'A')
inOrderTraversal(root)

#Python