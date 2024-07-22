# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa: A002
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        prev = None
        while p is not None and p.next is not None:
            q = p.next
            temp = q.next
            q.next = p
            p.next = temp
            if prev is not None:
                prev.next = q
            else:
                head = q
            prev = q.next
            p = q.next.next
        return head
