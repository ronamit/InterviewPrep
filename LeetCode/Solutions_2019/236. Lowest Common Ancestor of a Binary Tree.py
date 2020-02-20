# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeClass import TreeNode, stringToTreeNode, SearchVal



def SearchAncestors(root, p):
    if not root:
        return []
    if root == p:
        return [p]
    else:
        r_out = SearchAncestors(root.right, p)
        l_out = SearchAncestors(root.left, p)
        # if at least one of the children finds v, then we add the current node to ancestors
        if r_out or l_out:
            return l_out + r_out + [root]
        else:
            return []

def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    p_anc = SearchAncestors(root, p)
    q_anc = SearchAncestors(root, q)
    p_anc_set = set(p_anc)
    for h, node in enumerate(q_anc):
        if node in p_anc_set:
            return node
    return -1




self = None
root = stringToTreeNode('[3,5,1,6,2,0,8,null,null,7,4]')
root.display()
p = SearchVal(root, 5)
q = SearchVal(root, 1)
print(lowestCommonAncestor(self, root, p, q).val)

