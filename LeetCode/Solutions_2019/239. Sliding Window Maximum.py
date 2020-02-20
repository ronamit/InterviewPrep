from heapq import  heappush, heappop

def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # O(n) solution
    h = [] # "min heap"
    outList = []
    n = len(nums)
    for i in range(n):
        heappush(h, (-nums[i], i))
        # the minus is because this is a min-heap and we need max
        if i < k - 1:
            continue
        else:
            print(h)
            winMax = heappop(h)
            while i - winMax[1] > k - 1:
                winMax = heappop(h)
            outList += [-winMax[0]]
            # return to the heap for future use:
            if i - winMax[1] < k - 1:
                heappush(h, winMax)
            # # delete old values:
            # for elem in h:
            #     if elem[1] < i - k:
            #         h.remove(elem)
    return outList


self = None
nums = [9,10,9,-7,-4,-8,2,-6]
k = 5
print(maxSlidingWindow(self, nums, k))