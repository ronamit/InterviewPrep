from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_childs(node):
    childs = []
    if node.left:
        childs.append(node.left)
    if node.right:
        childs.append(node.right)
    return childs


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        left_queue = deque([root.left])
        right_queue = deque([root.right])
        while left_queue and right_queue:
            left_node = left_queue.pop()
            right_node = right_queue.pop()
            if left_node is None and right_node is None:
                continue
            if left_node is None or right_node is None:
                return False
            if left_node.val != right_node.val:
                return False
            left_queue.appendleft(left_node.left)
            left_queue.appendleft(left_node.right)
            right_queue.appendleft(right_node.right)
            right_queue.appendleft(right_node.left)
        return not left_queue and not right_queue
