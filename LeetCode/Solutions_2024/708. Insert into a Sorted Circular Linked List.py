# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):  # noqa: A002
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node | None, insertVal: int) -> Node:

        # in case of an empty list
        if head is None:
            node = Node(val=insertVal, next=None)
            node.next = node
            head = node
            return head

        # in case of single element list
        if head.next == head:
            node = Node(val=insertVal, next=head)
            head.next = node
            return head

        cur_node = head
        seen_nodes = set()
        while True:
            seen_nodes.add(cur_node)
            # in case we insert between two non-decreasing nodes
            if cur_node.val <= insertVal <= cur_node.next.val:
                node = Node(val=insertVal, next=cur_node.next)
                cur_node.next = node
                return head
            # in case of insert after loop reset
            if cur_node.next.val < cur_node.val and (insertVal >= cur_node.val or insertVal < cur_node.next.val):
                node = Node(val=insertVal, next=cur_node.next)
                cur_node.next = node
                return head
            if cur_node.next in seen_nodes:
                # in case we reached here, it means all values in the list are equal, or the loop reset is in the head
                # so we need t insert before the head
                node = Node(val=insertVal, next=cur_node.next)
                cur_node.next = node
                return head
            cur_node = cur_node.next
