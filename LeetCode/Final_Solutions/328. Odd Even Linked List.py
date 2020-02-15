from LinkedList import  ListNode, stringToLinkedList, LinkedListToList

def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None
    odd_tail = head
    n_pre_even = head.next
    if n_pre_even is None:
        return head
    np = head.next.next
    while np is not None:
        p = np
        pre_even = n_pre_even
        if p.next is not None:
            np = p.next.next
            n_pre_even = p.next
        else:
            np = None
        pre_even.next = p.next
        tp = odd_tail.next
        odd_tail.next = p
        p.next = tp
        odd_tail = p
    return head



self = None
input = '1->2->3->4->5->NULL'
head = stringToLinkedList(input, separator='->')
head = oddEvenList(self, head)
print(LinkedListToList(head))

