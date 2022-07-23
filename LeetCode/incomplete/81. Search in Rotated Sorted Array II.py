from typing import List, Dict, Tuple, Sequence
import itertools, collections


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        # find pivot index
        left = 0
        right = n - 1
        pivot = 0
        while right > left:
            mid = (left + right) // 2
            prev_val = nums[(mid - 1) % n]
            mid_val = nums[mid]
            left_val = nums[left]
            if mid_val < prev_val:
                pivot = mid
                break
            elif left_val < mid_val:
                left = mid + 1
            else:
                right = mid - 1
        print('Pivot: ', pivot)
        # search in the rotated array
        left = 0
        right = n - 1
        while right > left:
            mid_idx = (left + right) // 2
            mid_val = nums[(mid_idx + pivot) % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        return False

#-------------------------------------------------------------------------------
#
# nums = [2,5,6,0,0,1,2]
# target = 0

# nums = [2,5,6,0,0,1,2]
# target = 3

nums = [1,0,1,1,1]
target = 0

s = Solution()
print(s.search(nums, target))