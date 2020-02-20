class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(filter(lambda x: x > 0, nums))
        nums_set = set(nums)
        i = 1
        while True:
            if i not in nums_set:
                return i
            else:
                i += 1
