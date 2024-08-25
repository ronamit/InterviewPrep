# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        def scan_tree(node: TreeNode):
            # Returns:  the the number of uni-value subtrees, and the univalue in case the root is uni-value, else None
            if not node:
                return 0, None
            if not node.left and not node.right:
                # leaf
                return 1, node.val
            left_univals_count, left_unival = scan_tree(node.left)
            right_univals_count, right_unival = scan_tree(node.right)
            unival_count = left_univals_count + right_univals_count
            node_unival = None
            child_univals = []
            if node.left:
                child_univals.append(left_unival)
            if node.right:
                child_univals.append(right_unival)
            if all([v == child_univals[0] for v in child_univals]) and child_univals[0] == node.val:
                node_unival = node.val
                unival_count += 1
            return unival_count, node_unival

        unival_count, node_unival = scan_tree(root)
        return unival_count
