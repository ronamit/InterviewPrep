# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import LinkedListToList

def FlipFirstK(head, k):
    # flipping order of the first k nodes:
    if head is None:
        return
    p = head.next
    old_head = head
    if p is None:
        return
    for i in range(1, k):
        # remove p:
        pnext = p.next
        old_head.next = pnext
        # put p as head :
        prev_head = head
        head = p
        head.next = prev_head
        p = pnext
    return head

def ListLen(head):
    p = head
    n = 0
    while p is not None:
        p = p.next
        n += 1
    return n

def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # how to do it in O(1) space -  change the list itself, flipping order of one of the halves,
    # then go with two pointers...
    n = ListLen(head)
    if n==0: return True
    head = FlipFirstK(head, n//2)
    p2 = head
    for j in range((n-1)//2+1):
        p2 = p2.next
    p1 = head
    for i in range(n // 2):
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

#--------------------------------------------------------------------------------------------------------
from LinkedList import stringToLinkedList
input = '[1,2,3,2,1]'
head = stringToLinkedList(input)
print(LinkedListToList(head))  # DEBUG
self = None
print(isPalindrome(self, head))