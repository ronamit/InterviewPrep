# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans = [[]]
        que1 = deque([root])
        que2 = deque()
        while que1:
            node = que1.pop()
            ans[-1].append(node.val)
            if node.left is not None:
                que2.appendleft(node.left)
            if node.right is not None:
                que2.appendleft(node.right)
            if not que1 and que2:
                ans.append([])
                que1 = que2
                que2 = deque([])
        return ans
