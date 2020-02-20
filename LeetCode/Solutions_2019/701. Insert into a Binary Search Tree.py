from TreeClass import TreeNode, stringToTreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def insertIntoBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    def InsertFunc(t, x):
        if t is None:
            return TreeNode(x)
        if t.val > x:
            if t.left is None:
                t.left = TreeNode(x)
            else:
                InsertFunc(t.left, x)
        elif t.val < x:
            if t.right is None:
                t.right = TreeNode(x)
            else:
                InsertFunc(t.right, x)
        else:
            raise ValueError
        return t

    return InsertFunc(root, val)


self = None
root = stringToTreeNode('[40,20,60,10,30,50,70]') #   ('[4,2,7,1,3]')
root.display()
val = 25 # 5
new_t = insertIntoBST(self, root, val)
new_t.display()
