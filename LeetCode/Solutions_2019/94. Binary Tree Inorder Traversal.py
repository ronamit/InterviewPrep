# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sol = []
        if root is None: return []
        stack = [root]
        p = root
        # idea: when a a node is inserted to stack, then we immediately after insert all the left decendents
        while p.left is not None:
            stack.append(p.left)
            p = p.left

        while stack != []:
            p = stack.pop()
            self.sol += [p.val]
            if p.right is not None:
                p = p.right
                stack.append(p)
                while p.left is not None:
                    p = p.left
                    stack.append(p)

        return self.sol

    # Recoursion:
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     self.sol = []
    #     def inorderTraversalR(root):
    #         if root is None: return
    #         inorderTraversalR(root.left)
    #         self.sol += [root.val]
    #         inorderTraversalR(root.right)
    #     inorderTraversalR(root)
    #     return self.sol