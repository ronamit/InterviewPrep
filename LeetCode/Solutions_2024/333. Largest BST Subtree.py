# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        largest_size = 0

        def scan_tree(node: TreeNode | None):
            nonlocal largest_size
            if not node:
                return True, +float("inf"), -float("inf"), 0
            is_left_bst, left_min, left_max, left_size = scan_tree(node.left)
            is_right_bst, right_min, right_max, right_size = scan_tree(node.right)
            is_cur_bst = is_left_bst and is_right_bst and left_max < node.val < right_min
            cur_size = left_size + right_size + 1
            cur_max = max(node.val, left_max, right_max)
            cur_min = min(node.val, left_min, right_min)
            if is_cur_bst:
                largest_size = max(largest_size, cur_size)
            return is_cur_bst, cur_min, cur_max, cur_size

        scan_tree(root)
        return largest_size
