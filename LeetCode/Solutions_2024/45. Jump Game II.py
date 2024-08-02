import math


class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        min_to_end = [math.inf for _ in range(n)]
        min_to_end[n - 1] = 0
        for i in range(n - 2, -1, -1):
            # the max length of jump from i
            max_jump = min(nums[i], n - i - 1)
            # the min number of jumps is min over the possible jumps j of 1 + min_to_end[i+j]
            for j in range(1, max_jump + 1):
                min_to_end[i] = min(min_to_end[i], 1 + min_to_end[i + j])
        return min_to_end[0]
