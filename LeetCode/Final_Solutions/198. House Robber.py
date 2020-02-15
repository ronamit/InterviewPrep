class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        V = [0 for _ in range(n)]
        if n == 0:
            return 0
        V[0] = nums[0]
        for i in range(1, n):
            if i >= 2:
                V[i] = max(nums[i] + V[i - 2], V[i - 1])
            else:
                V[i] = max(nums[0], nums[1])
        return max(V)

