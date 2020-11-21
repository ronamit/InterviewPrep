
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
        if val in self.val2node:
            return  # allow only one node with value val
        predecessor = p
        successor = p.next
        newest = ListNode(val, predecessor,  successor)
        self.val2node[val] = newest
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
    # end def

    def insert_before_pointer(self, p, val):
       self.insert_before_pointer(p.prev, val)
    # end def


    def insert_after_value(self, val, new_val):
        p = self.get_pointer(val)
        if p is None:
            # in case val not in list, insert after header
            p = self.header
        if p.next.val == new_val:
            return # nothing to be done
         # end if
        self.insert_after_pointer(p, new_val)
    # end def

    def insert_before_value(self, val, new_val):
        p = self.get_pointer(val)
        if p is None:
            # in case val not in list, insert before trailer
            p = self.trailer
        if p.prev.val == new_val:
            return # nothing to be done
         # end if
        self.insert_before_pointer(p, new_val)
    # end def

    def get_val_prev_to_val(self, val):
        p = self.get_pointer(val)
        return p.prev.val


    def insert_at_head(self, val):
        return self.insert_after_pointer(self.header, val)
    # end def

    def remove_node(self, p):
        p.next.prev = p.prev
        p.prev.next = p.next
        self.size -= 1
        del self.val2node[p.val]
    # end def

    def delete_node(self, p):
        self.remove_node(p)
        del p
    # end def

    def delete_val(self, val):
        p = self.get_pointer(val)
        self.delete_node(p)
    # end def

    def __str__(self):
        # prints elements (without header and trailer)
        out_str = '['
        p = self.header.next
        seen = {p}
        while p.next is not None:
            out_str += str(p.val) + ', '
            p = p.next
            assert p not in seen  # infinite loop
        # end while
        if len(out_str) > 1:
            out_str = out_str[:-2]
        out_str = out_str + ']'
        return out_str
    # end def

# end class

if __name__ == "__main__":
    a = DoublyLinkedListUnique()
    print(a)
    a.insert_at_head(1)
    a.insert_at_head(2)
    a.insert_at_head(3)
    print(a)
    a.insert_after_value(2, 9)
    print(a)
    a.delete_val(2)
    print(a)
    a.insert_after_value(3, 8)
    print(a)
# end if