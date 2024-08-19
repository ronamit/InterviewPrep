# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def scan(t: TreeNode):
            # returns: number of equality nodes,  number of nodes, sum of nodes
            if t is None:
                return 0, 0, 0
            n_eq1, n1, s1 = scan(t.left)
            n_eq2, n2, s2 = scan(t.right)
            n = n1 + n2 + 1
            s = s1 + s2 + t.val
            n_eq = n_eq1 + n_eq2 + ((s // n) == t.val)
            return n_eq, n, s

        n_eq, n, s = scan(root)
        return n_eq
