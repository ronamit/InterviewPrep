from TreeClass import TreeNode, stringToTreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepthR(root):
    if root is None:
        return 0
    return 1 + max(maxDepthR(root.left),
                   maxDepthR(root.right))

def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return maxDepthR(root)


self = None
T = stringToTreeNode('[3,9,20,null,null,15,7]')
T.display()
print(maxDepth(self, T))