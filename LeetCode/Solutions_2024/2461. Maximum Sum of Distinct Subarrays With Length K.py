from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        sub_counts = defaultdict(lambda: 0)
        sub_sum = 0
        max_sum = 0
        for i, x in enumerate(nums):
            sub_sum += x
            sub_counts[x] += 1
            if i >= k:
                y = nums[i - k]
                sub_sum -= y
                sub_counts[y] -= 1
                if sub_counts[y] == 0:
                    del sub_counts[y]
            if len(sub_counts) == k:
                max_sum = max(max_sum, sub_sum)
        return max_sum
