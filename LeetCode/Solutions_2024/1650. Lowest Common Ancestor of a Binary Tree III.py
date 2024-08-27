from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:

        if p.val == q.val:
            return p
        not_q_ansectors = set()
        node = p
        while node:
            # check if node is ansector of q, and keep answers in is_ancestor_of_q, if so, return node
            if node.val == q.val:
                return node
            # BFS
            queue = deque([node])
            while queue:
                cur_node = queue.pop()
                if cur_node.val in not_q_ansectors:
                    # no need to scan again this sub-tree
                    continue
                if cur_node.left:
                    if cur_node.left.val == q.val:
                        return node
                    queue.appendleft(cur_node.left)
                if cur_node.right:
                    if cur_node.right.val == q.val:
                        return node
                    queue.appendleft(cur_node.right)
            # search for q failed
            not_q_ansectors.add(node.val)
            # go up
            node = node.parent
        return node
