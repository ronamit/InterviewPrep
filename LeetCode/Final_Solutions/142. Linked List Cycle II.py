# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        seen = set()
        p = head
        i = 0
        while p is not None:
            if p in seen:
                return p
            seen.add(p)
            p = p.next
        return None
