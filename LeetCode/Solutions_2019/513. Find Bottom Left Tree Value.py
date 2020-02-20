class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        def RecFunc(t, h):
            if not t.left and not t.right:
                return t.val, h
            rV = None
            lV = None
            if t.left:
                lV, lH = RecFunc(t.left, h + 1)
            if t.right:
                rV, rH = RecFunc(t.right, h + 1)
            if (rV is None) or (lV is not None and lH >= rH):
                return lV, lH
            else:
                return rV, rH

        v, h = RecFunc(root, 0)
        return v
