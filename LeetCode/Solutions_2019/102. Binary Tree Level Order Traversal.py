# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        sol = []

        def goDepth(p, depth):
            if p is None:
                return
            if len(sol) < (depth + 1):
                sol.append([])
            sol[depth].append(p.val)
            goDepth(p.left, depth + 1)
            goDepth(p.right, depth + 1)

        goDepth(root, 0)
        return sol
