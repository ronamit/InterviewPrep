from heapq import  heappush, heappop, heappushpop, heapify
import heapq
from collections import deque
from queue import PriorityQueue


class DequeWithGetMax:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = deque()
        self.cur_max = None

    def append(self, x):
        """
        :type x: int
        :rtype: void
        """
        if (self.cur_max is None) or (x > self.cur_max):
            self.cur_max = x
        self.q.append((x, self.cur_max))

    def popleft(self):
        """
        :rtype: void
        """
        if not self.q:
            return None
        x, x_max = self.q.popleft()
        if not self.q:
            self.cur_max = None
        else:
            self.cur_max = self.q[0][1]
        return x

    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.q.

    def getMin(self):
        """
        :rtype: int
        """
        return self.cur_max



def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # O(n) solution
    h = []  # "min heap"
    q = deque()  # "queue"
    outList = []
    n = len(nums)
    for i in range(n):
        # the minus is because this is a min-heap and we need max:
        newElem = -nums[i]
        # we add the element to both data structures
        # the que will make it possible to delete old elemnts (no need to keep more than k elements)
        # the heap will help to find the max
        heappush(h, newElem)
        q.append(newElem)
        if i < k - 1:
            continue
        else:
            print(i)
            print(h)
            print(q)
            # take the max from memory:
            winMax = h[0]
            print('max ' + str(-winMax))
            outList += [-winMax]
            # delete old values:
            if len(q) > k-1:
               oldElem = q.popleft()
               # TODO: We need a dec-key procedure to remove an item and keep heap valid
               # but it seems python doesn't support
               h.remove(oldElem)
               heapify(h)

    return outList


self = None
nums = [1,3,1,2,0,5]
k = 3
print(maxSlidingWindow(self, nums, k))