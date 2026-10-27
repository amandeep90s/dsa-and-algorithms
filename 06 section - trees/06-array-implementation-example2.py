# Store the binary tree in a list. For a node at index i, its children are
# at indices 2 * i + 1 (left) and 2 * i + 2 (right). None marks an empty spot.

binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

# Return the list index of the left child of the node at index.
def left_child_index(index):
    return 2 * index + 1

# Return the list index of the right child of the node at index.
def right_child_index(index):
    return 2 * index + 2

# Visit the current node, then its left subtree, then its right subtree.
# Return an empty list when the index is past the array or marks no node.
def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

# Visit the left subtree, then the current node, then the right subtree.
def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

# Visit the left subtree, then the right subtree, then the current node.
def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

# Start each depth-first traversal at index 0, the root of the tree.
print("Pre-order Traversal:", pre_order(0))
print("In-order Traversal:", in_order(0))
print("Post-order Traversal:", post_order(0))