# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = set()
        p = headA
        while p:
            visited.add(p)
            p = p.next
        p = headB
        while p:
            if p in visited:
                return p
            p = p.next
        return None