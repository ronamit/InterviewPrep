# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        out = []

        def Go(t, depth, out):
            if t is None:
                return
            if depth >= len(out):
                out.append([])
            out[depth].append(t.val)
            Go(t.left, depth + 1, out)
            Go(t.right, depth + 1, out)
            return

        Go(root, 0, out)
        return out