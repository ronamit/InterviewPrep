from LinkedList import ListNode, stringToLinkedList, LinkedListToList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    stack = []
    p = head
    while p is not None:
        stack.append(p)
        pnext = p.next
        p = pnext
    for i in range(n-1):
        pnext = stack.pop()
    p = stack.pop()
    if stack:
        pprev = stack.pop()
        pprev.next = pnext
    else:
        head = pnext
    del p
    return head

self = None
# input = '1->2->3->4->5'
# n = 2

input = '1'
n = 1


head = stringToLinkedList(input, separator='->')
head =removeNthFromEnd(self, head, n)
L = LinkedListToList(head)
print(L)