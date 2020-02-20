from LinkedList import ListNode, stringToLinkedList, LinkedListToList, LinkedListToList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    from heapq import heappop, heappush

    p = head
    heap = []
    n = 0
    while p is not None:
        n += 1
        heappush(heap, p.val)
        p_next = p.next
        del p
        p = p_next
    head = ListNode(0) # dummy head
    p = head
    for i in range(n):
        min_val = heappop(heap)
        print(min_val)
        p.next = ListNode(min_val)
        p = p.next
    return head.next




self = None
input = '[4->2->1->3]'
head = stringToLinkedList(input, separator='->')

print(LinkedListToList(head))

head = sortList(self, head)

print(LinkedListToList(head))



# def ListLen(p):
#     L = 0
#     while p is not None:
#         p = p.next
#         L += 1
#     return L
#
# def ListGoTo(p, steps):
#     for i in range(steps):
#         p = p.next
#     return p
#
#
# def MergeSort(head, start, end):
#     print(LinkedListToList(head))
#     n = end - start + 1
#     mid = (start + end) // 2
#     if n <= 1:
#         return head
#     else:
#         MergeSort(head, start, mid)
#         MergeSort(head, mid+1, end)
#         # Merge:
#         p1 = ListGoTo(head, start)
#         p2 = ListGoTo(head, mid+1)
#         n1 = mid - start + 1
#         n2 = end - mid
#         merge_lists(p1, n1, p2, n2)
#
#
#     return head
#
# def sortList(self, head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     return MergeSort(head, 0, ListLen(head)-1)

