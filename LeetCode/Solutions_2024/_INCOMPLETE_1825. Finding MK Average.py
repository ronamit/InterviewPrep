import heapq
from heapq import heappush, heappop, heappushpop


class MKAverage:
    """
    I solved by mistake the case where look at all history and not just the last m times..
    see a correct solution here:
    https://leetcode.com/problems/finding-mk-average/solutions/3938332/python3-keeping-three-containers-for-small-middle-large-values-runtime-98-memory-94/?envType=company&envId=google&favoriteSlug=google-thirty-days´


    Note that my solution can be correctd if we add a queue of the last m elements with a pointer to their node in the heaps so we can remove old elements in O(log(k))
    but it will require to implment the heap from scratch - to allow removing any elements (using sift-up and pop root)

    Solution idea:
    * we don't need to keep track of all the inserted numbers..
    just their sum and the the values of the k-bottom and k-top numbers
    seen
    we can keep those numbers in two heaps, max heap for the k-bottom
    and min heap for the k-top .
    we also keep a variable for the sum of each.
    when adding elemnt we insert it to one of them if needed. O(log(k))
    calculateMKAverage  is O(1) - total_sum - k_smallest_sum - k_largest_sum
    """

    def __init__(self, m: int, k: int):
        self.total_sum = 0
        self.total_count = 0
        self.k_smallest_sum = 0
        self.k_largest_sum = 0
        self.k_smallest_heap = []
        self.k_largest_heap = []
        self.max_of_smallest_k = None
        self.min_of_largest_k = None
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:

        self.total_count += 1
        self.total_sum += num
        if self.total_count <= self.k:
            # in this case - just add to each heap (no need to remove old values)
            heappush(self.k_largest_heap, num)  #  min-heap
            self.k_largest_sum += num
            heappush(self.k_smallest_heap, -num)  #  use minus to act as max-heap
            self.k_smallest_sum += num
        else:
            # in this case - add the correct heap and replace old value
            if num > self.min_of_largest_k:
                removed_num = heappushpop(self.k_largest_heap, num)  #  min-heap
                self.k_largest_sum += num - removed_num
            if num < self.max_of_smallest_k:
                #  use minus to act as max-heap:
                removed_num = heappushpop(self.k_smallest_heap, -num)
                self.k_smallest_sum += num - (-removed_num)
        # get from the heaps roots:
        self.min_of_largest_k = self.k_largest_heap[0]
        self.max_of_smallest_k = -self.k_smallest_heap[0]  # revert the minus

    def calculateMKAverage(self) -> int:
        if self.total_count < self.m:
            return -1
        middle_sum = self.total_sum - self.k_smallest_sum - self.k_largest_sum
        middle_count = self.total_count - 2 * self.k
        print(f"middle_sum = {middle_sum}, middle_count={middle_count}")
        return int(middle_sum / middle_count)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
