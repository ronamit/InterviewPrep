from TreeClass import TreeNode, stringToTreeNode

def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    # for each node fine the max path that ends with left node+current node
    # and same for right
    # to compute maxPath - go over all nodes and take the max of (maxL+maxR+node.val)

    def F(p):
        if p.left:
            LL, LR, mpL = F(p.left)
            # max path that ends with LeftSon->Root:
            maxL = p.left.val + max(LL, LR, 0)
            # the zero is for stopping the path after son
        else:
            mpL = None
            maxL = 0
        if p.right:
            RL, RR, mpR = F(p.right)
            # max path that ends with RightSon->Root:
            maxR = p.right.val + max(RL, RR, 0)

        else:
            mpR = None
            maxR = 0
        # max path that goes trough root (consider all options)
        mpRoot = max(p.val,  p.val + maxL,  p.val + maxR, p.val+maxL+maxR)
        # find max for all roots in the whole sub-tree:
        if mpL != None:
            mpRoot = max(mpRoot, mpL)
        if mpR != None:
            mpRoot = max(mpRoot, mpR)
        return maxL, maxR, mpRoot

    if not root:
        return 0
    maxL, maxR, mpRoot = F(root)
    return mpRoot

self = None
root = stringToTreeNode('[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]')
root.display()
print(maxPathSum(self, root))
