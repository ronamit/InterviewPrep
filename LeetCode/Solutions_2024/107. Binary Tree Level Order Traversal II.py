from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        cur_level = deque([root])
        levels: list[list] = []
        while True:
            levels.append([])
            next_level = deque()
            while cur_level:
                node = cur_level.pop()
                levels[-1].append(node.val)
                if node.left:
                    next_level.appendleft(node.left)
                if node.right:
                    next_level.appendleft(node.right)
            if len(next_level) == 0:
                break
            cur_level = next_level
        return levels[::-1]
