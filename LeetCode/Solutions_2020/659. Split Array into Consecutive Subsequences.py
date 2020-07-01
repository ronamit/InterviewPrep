from typing import List, Dict, Tuple, Sequence
import itertools

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = [[grp[0], len(list(grp[1]))] for grp in itertools.groupby(nums)]
        n = len(counts)
        for i, (num_i, count_i) in enumerate(counts):
            if count_i == 0:
                continue
            shift = 0
            while shift < n-1:
                j = i + shift
                if j > n-1:
                    break
                num_j, count_j = counts[j]
                if num_j != (num_i + shift) or count_j < count_i:
                    return False
                else:
                    counts[j][1] -= count_i
            if shift < 3:
             i += 1
        return True


nums = [1,2,3,3,4,4,5,5]
sol = Solution()
print(sol.isPossible(nums))