from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in prev_nums:
                return i, prev_nums[y]
            prev_nums[x] = i
        return None
