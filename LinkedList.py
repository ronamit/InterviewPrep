

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def stringToLinkedList(input, separator=','):
    input = input.strip()
    if input[0] == '[' and input[-1] == ']':
        input = input[1:-1]
    if not input:
        return None
    values = [s.strip() for s in input.split(separator)]
    if values[-1] == 'NULL':
        values = values[:-1]
    # make int:
    values = [int(x) for x in values]
    return ListToLinkedList(values)



def ListToLinkedList(values):
    n = len(values)
    if n == 0:
        return None
    head = ListNode(values[0])
    p = head
    for i in range(1,n):
        p.next = ListNode(values[i])
        p = p.next
    return head


def LinkedListToList(head):
    lst = []
    p = head
    visits = set()
    while p is not None:
        if p in visits:
            raise ValueError('Invalid Linked List!!')
        visits.add(p)
        lst.append(p.val)
        p = p.next
    return lst
