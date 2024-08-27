class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        max_possible_ind = 0
        for i in range(n):
            if i > max_possible_ind:
                break
            max_dest = i + nums[i]
            max_possible_ind = max(max_possible_ind, max_dest)
            if max_possible_ind >= n - 1:
                return True
        return False
