import math


class Element:
    def __init__(self, val: int):
        self.val = val
        # save a pointer to the the element with value one above in the sorted order
        self.next_up = None


class MinStack:

    def __init__(self):
        self.stk = []
        self.min_elem = Element(math.inf)

    def push(self, val: int) -> None:
        x = Element(val)
        self.stk.append(x)
        if x.val < self.min_elem.val:
            x.next_up = self.min_elem
            self.min_elem = x

    def pop(self) -> None:
        if self.stk[-1] == self.min_elem:
            self.min_elem = self.min_elem.next_up
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1].val

    def getMin(self) -> int:
        return self.min_elem.val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
