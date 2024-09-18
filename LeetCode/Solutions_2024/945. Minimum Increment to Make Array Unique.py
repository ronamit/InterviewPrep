from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)
        heap = list(counts.keys())
        heapify(heap)  # min - heap
        seen_nums = set()
        ans = 0
        while heap:
            x = heappop(heap)
            if x in seen_nums:
                continue
            seen_nums.add(x)
            cnt = counts[x]
            if cnt > 1:
                counts[x] = 1
                counts[x + 1] += cnt - 1
                if x + 1 not in seen_nums:
                    heappush(heap, x + 1)
                ans += cnt - 1
        return ans
