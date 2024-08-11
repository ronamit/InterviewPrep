import numpy as np


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        # Naive O(n^2 * log(n))

        prefix_sum = np.cumsum(nums)

        new_nums = []
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    new_nums.append(nums[i])
                elif i == 0:
                    new_nums.append(prefix_sum[j])
                else:
                    new_nums.append(prefix_sum[j] - prefix_sum[i - 1])
        new_nums = np.array(new_nums)
        new_nums.sort()
        mod = 10**9 + 7
        ans = 0
        for i in range(left - 1, right):
            ans = (ans + new_nums[i]) % mod
        return ans
