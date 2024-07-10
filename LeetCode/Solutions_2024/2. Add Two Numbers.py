# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans_head = None
        prev_node = None
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            l1_v = l1.val if l1 is not None else 0
            l2_v = l2.val if l2 is not None else 0
            s = l1_v + l2_v + carry
            new_node = ListNode(val=s % 10)
            carry = s // 10
            if prev_node is not None:
                prev_node.next = new_node
            else:
                ans_head = new_node
            prev_node = new_node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return ans_head
