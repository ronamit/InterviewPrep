import numpy as np


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles = np.array(piles)
        # binary search
        left = 1
        right = piles.max()
        while left < right:
            mid = (right + left) // 2
            # check if mid is an eating speed that is enough to eat all in the time limit:
            if np.ceil(piles / mid).sum() <= h:
                right = mid
            else:
                left = mid + 1
        return left
