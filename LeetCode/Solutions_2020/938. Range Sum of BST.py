# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from LeetCode.TreeClass import TreeNode

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def RecFunc(t):
            if t is None:
                return 0
            if t.val >= L and t.val <= R:
                s = t.val
            else:
                s = 0
            s += RecFunc(t.left) + RecFunc(t.right)
            # TODO: make more efficent by not calling all childs (still O(n) though)
            return s

        return RecFunc(root)
