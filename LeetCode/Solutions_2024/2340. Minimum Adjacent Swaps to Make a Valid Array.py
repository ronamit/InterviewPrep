class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # find the first min and last max
        min_val = nums[0]
        i_min = 0
        max_val = nums[0]
        i_max = 0
        n = len(nums)
        for i in range(1, n):
            x = nums[i]
            if x < min_val:
                min_val = x
                i_min = i
            if x >= max_val:
                max_val = x
                i_max = i
        if i_min <= i_max:
            return i_min + (n - 1 - i_max)
        return i_min + (n - 1 - i_max) - 1
