import math


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        cum_sum = 0
        ans = 0
        for i, x in enumerate(nums):
            cum_sum += x
            avg_val = cum_sum / (i + 1)
            ans = max(ans, math.ceil(avg_val))
        return ans
