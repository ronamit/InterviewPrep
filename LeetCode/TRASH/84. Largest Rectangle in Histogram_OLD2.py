def largestRectangleArea(self, heights):

    def LastBelowTarget(arr, target):
        n = len(arr)
        low = 0
        high = n - 1
        while high >= low:
            mid = (low + high) // 2
            x = arr[mid][0]
            if x <= target and (mid == n-1 or arr[mid+1][0] > target):
                return mid
            if x < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    n = len(heights)
    max_area = 0
    stk = []
    # the stack will keep for each height - how far back (from which index) can we go with this height
    for i, h in enumerate(heights):
        start = i
        while stk and stk[-1][0] > h:
            # if the bin is higher than h - we can discard it
            # but, we can start the rectengle at this location
            start = min(stk[-1][1],  start)
            stk.pop()
        stk.append((h, start))

        # the heights in the  stk are sorted in ascending order
        # use binary search to find the first element which is lower or equal to h
        ind = LastBelowTarget(stk, h)
        hh, ii = stk[ind]
        area = hh * (i - ii + 1)

        hstk = [hh for (hh, ii) in stk]
        istk = [ii for (hh, ii) in stk]
        areas = [hh*(i-ii+1) for (hh, ii) in stk]
        # area = max(areas)

        max_area = max(max_area, area)
    return max_area

self = None
heights = [2,1,5,6,2,3]
# heights = [1,2,3,4,5]
print(largestRectangleArea(self, heights))

