from TreeClass import TreeNode, stringToTreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    # note - if each node had the number of nodes in its sub-tree, we could have O(height) solution
    lst = []
    def RecFunc(p):
        nonlocal k, lst
        if not p:
            return
        RecFunc(p.left)
        lst += [p.val]
        print(p.val)
        RecFunc(p.right)
    RecFunc(root)
    return lst[k-1]

self = None
input = '[3,1,4,null,2]'
k = 1
root = stringToTreeNode(input)
print(kthSmallest(self, root, k))
