from typing import List
""""
see better solution in O(n): https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/solutions/4322342/o-n-consice-easy-to-understand-solution-in-python3/
"""

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        index_val_sorted = [i_v for i_v in sorted(enumerate(nums), key=lambda x:x[1])]   
        # since we want decreasing sub array - reverse order:
        index_val_sorted.reverse()
        
        # loop over the sorted list of index-value pairs, and find for each index the min so far
        min_idx_so_far = index_val_sorted[0][0]
        max_sub_len = 0
        print(index_val_sorted)
        for orig_idx, val in index_val_sorted:
            min_idx_so_far = min(min_idx_so_far, orig_idx)
            if min_idx_so_far < orig_idx:
                max_sub_len = max(max_sub_len, orig_idx - min_idx_so_far + 1)                        
        
        return max_sub_len


if __name__ == "__main__":
    # nums =[-994,-531,-544,935,-831,-671]
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.maxSubarrayLength(nums))
    
    
    
    # def maxSubarrayLength(self, nums: List[int]) -> int:
    #     i = 0
    #     j = len(nums) - 1
    #     while j > i:
    #         if  (nums[j] < nums[i]):
    #             return (j - i + 1)
    #         if nums[j - 1]  < nums[j]:
    #             j -= 1
    #         else:
    #             i += 1
    #     return 0
