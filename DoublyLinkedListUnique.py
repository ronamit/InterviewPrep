
class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.next = next
        self.prev = prev
    # end def
# end class

class DoublyLinkedListUnique : # source: http://xpzhang.me/teach/DS19_Fall/slide07.pdf
    # This is a variant of doubly linked list that keeps each value only once (no value repetitions)
    def __init__(self):
        self.header = ListNode(None, None, None)
        self.trailer = ListNode(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        self.val2node = dict()
    # end def

    def __len__(self):
        return self.size
    # end def

    def is_empty(self):
        return self.size == 0
    # end def

    def get_pointer(self, val):
        # returns a pointer for the element in the list with value val (None if there is no such element)
        if val not in self.val2node:
            return None
        else:
            return self.val2node[val]
        # end if
    # end def

    def insert_after_pointer(self, p, val):
        assert val not in self.val2node # allow only one node with value val
        predecessor = p
        successor = p.next
        newest = ListNode(val, predecessor,  successor)
        self.val2node[val] = newest
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
    # end def

    def insert_after_value(self, val, new_val):
        p = self.get_pointer(val)
        if p.next.val == new_val:
            return # nothing to be done
         # end if
        self.insert_after_pointer(p, new_val)
    # end def

    def insert_at_head(self, val):
        return self.insert_after_pointer(self.header, val)
    # end def

    def remove_node(self, p):
        p.prev = p.next
        p.next.prev = p.prev
        self.size -= 1
    # end def

    def delete_node(self, p):
        self.remove_node(p)
        del p
    # end def

    def delete_val(self, val):
        p = self.get_pointer(val)
        self.delete_node(p)
    # end def

    def print(self):
        # prints elements (without header and trailer)
        out_str = '['
        p = self.header.next
        seen = {p}
        while p.next is not None:
            out_str += str(p.val) + ', '
            p = p.next
            assert p not in seen # infinite loop
        # end while
        out_str = out_str[:-2] + ']'
        print(out_str)
        return out_str
    # end def
# end class

if __name__ == "__main__":
    a = DoublyLinkedListUnique()
    a.insert_at_head(1)
    a.insert_at_head(2)
    a.insert_at_head(3)
    a.print()
    a.insert_after_value(2, 9)
    a.print()
    a.delete_val(2)
    a.print()

# end if