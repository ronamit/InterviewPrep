from LinkedList import stringToLinkedList, ListNode, LinkedListToList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



def mergeTwoLists(l1, l2):
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



def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists: return []
    while len(lists) > 1:
        new_lists = []
        for i in range(len(lists) // 2):
            new_lists.append(mergeTwoLists(lists[2*i], lists[2*i+1]))
        if len(lists) % 2 == 1:
            # add last:
            new_lists.append(lists[-1])
        del lists
        lists = new_lists

    return lists[0]




self = None

lists_str = [ "[1->4->5]",
              "[1->3->4]",
              "[2->6]"]
lists = [stringToLinkedList(s, separator='->') for s in lists_str]
new_list = mergeKLists(self, lists)

print(LinkedListToList(new_list))