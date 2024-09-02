class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums  = sorted(nums)
        i_first_in_sorted = {}
        i_last_in_sorted = {}
        for i, x in enumerate(sorted_nums):
            if x not in i_first_in_sorted:
                i_first_in_sorted[x] = i
            i_last_in_sorted[x] = i
        
        start = None
        for i in range(n):
            if i_first_in_sorted[nums[i]] > i:
                start = i - 1
                break
        if start is None:
            return 0
        end = None
        for i in range(n - 1, -1, -1):
            if i_last_in_sorted[nums[i]] < i:
                end = i
                break
        if end is None:
            return 0
        return end - start

        
