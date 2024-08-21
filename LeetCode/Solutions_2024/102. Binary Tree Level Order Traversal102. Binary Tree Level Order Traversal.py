# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
#         if root is None:
#             return []
#         ans = [[]]
#         que1 = deque([root])
#         que2 = deque()
#         while que1:
#             node = que1.pop()
#             ans[-1].append(node.val)
#             if node.left is not None:
#                 que2.appendleft(node.left)
#             if node.right is not None:
#                 que2.appendleft(node.right)
#             if not que1 and que2:
#                 ans.append([])
#                 que1 = que2
#                 que2 = deque([])
#         return ans


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        n_nodes_in_level = 1
        while queue:
            ans.append([])
            for _ in range(n_nodes_in_level):
                node = queue.pop()
                ans[-1].append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            n_nodes_in_level = len(queue)
        return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))
