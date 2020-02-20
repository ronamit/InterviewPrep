from TreeClass import TreeNode, stringToTreeNode
def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root: return True
    stk1 = [root]  # stack for pre-order  - left first
    stk2 = [root] # stack for pre-order  - right first
    while stk1 and stk2:
        p1 = stk1.pop()
        p2 = stk2.pop()
        r1 = r2 = l1 = l2 = False
        if p1.right:
            stk1.append(p1.right)
            r1 = True
        if p2.left:
            stk2.append(p2.left)
            l2 = True
        if p1.val != p2.val:
            return False
        if p1.left:
            stk1.append(p1.left)
            l1 = True
        if p2.right:
            stk2.append(p2.right)
            r2 = True
        if (r1 != l2) or (r2 != l1):
            return False
    return (not stk1 and not stk2)



self = None
root = stringToTreeNode('[1,2,2,null,3,3]')
root.display()
print(isSymmetric(self, root))