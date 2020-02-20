# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def SearchFunc(t, x):
            if t == None:
                return None
            if t.val == x:
                return t
            elif t.val > x:
                return SearchFunc(t.left, x)
            else:
                return SearchFunc(t.right, x)

        return SearchFunc(root, val)