from typing import List, Dict, Tuple, Sequence

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Solution2 O(n):
        n = len(nums)
        sums = [a for a in nums]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        counter = 0
        prev_sums = {0: 1}
        for j in range(n):
            if (sums[j] - k) in prev_sums.keys():
                counter += prev_sums[sums[j] - k]
            if sums[j] in prev_sums.keys():
                prev_sums[sums[j]] += 1
            else:
                prev_sums[sums[j]] = 1
        return counter

        # Solution1: O(n^2)
        # n = len(nums)
        # sums = [a for a in nums]
        # for i in range(1,n):
        #     sums[i] = sums[i-1] + nums[i]
        # counter = 0
        # for j in range(n):
        #     if sums[j] == k:
        #         counter += 1
        #     for i in range(j):
        #         if (sums[j] - sums[i]) == k:
        #             counter +=1
        # return counter

