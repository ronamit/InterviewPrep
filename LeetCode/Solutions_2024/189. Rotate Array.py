class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_nums = [None for _ in range(n)]
        k = k % n
        for i in range(n):
            new_nums[i] = nums[i-k]
            print(nums[i-k])
        for i in range(n):
            nums[i] = new_nums[i]

        