from collections import Counter
from functools import cache


class Solution:

    def canPartition(self, nums: list[int]) -> bool:

        s = sum(nums)

        if s % 2 == 1:
            return False

        nums_count = list(Counter(nums).items())
        n_uniq_vals = len(nums_count)

        @cache
        def exist_subset(i: int, s_sub: int):
            # return true of if we can select a subset of the nums in nums_count[i:] with sum s1.
            nonlocal nums_count
            if i == n_uniq_vals:
                return s_sub == 0

            if s_sub < 0:
                # not possible subset - since no negative numbers
                return False
            x, x_cnt = nums_count[i]
            # we need to check all possible number of times we include x
            x_sum_in_sub = 0
            # The sum from i, after we omit the i-th possible numer from nums_count
            for _ in range(x_cnt + 1):
                if exist_subset(i=i + 1, s_sub=s_sub - x_sum_in_sub):
                    return True
                x_sum_in_sub += x
            return False

        return exist_subset(i=0, s_sub=s // 2)
