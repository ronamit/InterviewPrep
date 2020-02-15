# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        head = p.next
        pprev = head
        while p and p.next is not None:
            p2 = p.next.next
            p1 = p.next
            pprev.next = p1
            p.next = p2
            p1.next = p
            p = p2
            pprev = p
        return head
