class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        # M at index k = max sum of subarrays that ends exactly at k
        M = [nums[0]]
        for k in range(1, n):
            M.append(max(M[-1] + nums[k], nums[k]))
        return max(M)
