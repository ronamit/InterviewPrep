from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):  # noqa: A002
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:

        if not root:
            return None
        queue = deque([root])
        n_nodes_level = len(queue)

        while n_nodes_level > 0:
            for _ in range(n_nodes_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            n_nodes_level = len(queue)

            for i_node in range(n_nodes_level - 1):
                queue[i_node].next = queue[i_node + 1]
        return root
