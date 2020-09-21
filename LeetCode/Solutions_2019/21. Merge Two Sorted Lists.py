from  LinkedList import ListNode, stringToLinkedList ,LinkedListToList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    new_lst = ListNode(0) # dummy head
    p = new_lst
    while (l1 is not  None or l2 is not None):
        if l2 is None:
            p.next = l1
            l1 = l1.next
        elif l1 is None:
            p.next = l2
            l2 = l2.next
        elif l1.val > l2.val:
            p.next = l2
            l2 = l2.next
        else:
            p.next = l1
            l1 = l1.next

        p = p.next

    return new_lst.next


self = None
in1, in2 = '[1->2->4]', '[1->3->4]'
l1 = stringToLinkedList(in1, separator='->')
l2 = stringToLinkedList(in2, separator='->')
new_lst = mergeTwoLists(self, l1, l2)

new_lst = LinkedListToList(new_lst)
print(new_lst)

