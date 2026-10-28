# Binary Tree Implementation
# The Binary Tree above can be implemented much like we implemented a Singly Linked List, 
# except that instead of linking each node to one next node, 
# we create a structure where each node can be linked to both its left and right child nodes.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print(f"root.right.left.data: {root.right.right.data}")