from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        # col index = sum the go left with -1 and go right with +1 in the path from root to node
        if root is None:
            return []

        col_dict = {}  # col index : node val

        # run BFS, so that adding nodes will be ordered by rows/layers
        queue = deque([(root, 0)])  # tuples of node and col_idx

        while queue:
            node, col_idx = queue.pop()
            col_dict[col_idx] = [*col_dict.get(col_idx, []), node.val]
            if node.left:
                queue.appendleft((node.left, col_idx - 1))
            if node.right:
                queue.appendleft((node.right, col_idx + 1))

        min_idx = min(col_dict.keys())
        max_idx = max(col_dict.keys())
        ans = []
        for col_idx in range(min_idx, max_idx + 1):
            if col_idx in col_dict:
                ans.append(col_dict[col_idx])
        return ans
