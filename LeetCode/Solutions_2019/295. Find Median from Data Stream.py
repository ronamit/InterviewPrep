from heapq import heappush, heappop


# Idea: maxHeap saves the smaller half elements, minHeap the larger half
# |minHeap|  <= |maxHeap| <=  |minHeap| + 1

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxH = []
        self.minH = []

    def findMedian(self) -> float:
        a = -self.maxH[0]
        if len(self.minH) == len(self.maxH):
            b = self.minH[0]
            return (a + b) / 2
        else:
            return a * 1.0

    def addNum(self, num: int) -> None:

        if not self.maxH or num <= -self.maxH[0]:
            heappush(self.maxH, -num)
        else:
            heappush(self.minH, num)

        if len(self.minH) > len(self.maxH):
            a = heappop(self.minH)
            heappush(self.maxH, -a)
        elif len(self.maxH) > (len(self.minH) + 1):
            a = -heappop(self.maxH)
            heappush(self.minH, a)

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())
