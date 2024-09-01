# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        longest_ever = 0

        def dfs(node: TreeNode, go_left: bool, steps: int):
            nonlocal longest_ever
            # in any case, we must call both childs since longest_ever can be in any of them
            if not node:
                return
            longest_ever = max(longest_ever, steps)
            if go_left:
                dfs(node.left, False, steps + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, steps + 1)

        dfs(root, False, steps=0)
        dfs(root, True, steps=0)
        return longest_ever
