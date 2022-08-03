# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

import math
from typing import List, Dict, Tuple, Sequence
import itertools, collections

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # we want to find the max len of subarray with even num of negatives
        n = len(nums)
        num_neg_in_cur_sub = 0
        max_len_ends_cur = [0 for _ in range(n)] # each index holds the max len of subarray with even num of negatives that ends at the index
        prev_len_ends_cur = 0
        for i in range(n):
            if nums[i] > 0:
                # extend sub by 1
                max_len_ends_cur[i] = prev_len_ends_cur + 1
            elif nums[i] < 0:
                if num_neg_in_cur_sub % 2 == 0:
                    # start a new sub
                    num_neg_in_cur_sub = 1
                    max_len_ends_cur[i] = 0
                else:
                    # extend sub by 1
                    max_len_ends_cur[i] = prev_len_ends_cur + 1
                    num_neg_in_cur_sub += 1
            else: # nums[i] == 0
                # start a new sub
                num_neg_in_cur_sub = 0
                max_len_ends_cur[i] = 0
            prev_len_ends_cur = max_len_ends_cur[i]
        return max(max_len_ends_cur)





sol = Solution()
print(sol.getMaxLen( [-1,-2,-3,0,1]))
