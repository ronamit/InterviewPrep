# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random 

class Solution:

    def __init__(self, head: Optional[ListNode]): # type: ignore
        self.n = 0
        self.head = head
        p = head
        while p is not None:
            self.n += 1
            p = p.next
        

    def getRandom(self) -> int:
        n_steps = random.randint(0, self.n - 1)
        p = self.head
        while n_steps > 0:
            p = p.next
            n_steps -= 1
        return p.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()