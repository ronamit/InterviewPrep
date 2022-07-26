# better solution: https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
import math
from typing import List, Dict, Tuple, Sequence
import itertools, collections

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jmp2last = [math.inf for _ in range(n)]
        min_jmp2last[-1] = 0
        for i in range(n - 2, -1, -1):
            max_j = min(n - 1, i + nums[i])
            for j in range(i + 1, max_j + 1):
                min_jmp2last[i] = min(min_jmp2last[i], 1 + min_jmp2last[j])
        return int(min_jmp2last[0])



x = [2,3,1,1,4]
sol = Solution()
print(sol.jump(x))