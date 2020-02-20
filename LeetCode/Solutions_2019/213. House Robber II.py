
class Solution:
    def rob(self, nums: List[int]) -> int:

        def Rob1(first, length):
            if length <= 0:
                return 0
            V = [0 for _ in range(length)]
            V[0] = nums[first + 0]
            for i in range(1, length):
                if i >= 2:
                    V[i] = max(nums[first + i] + V[i - 2], V[i - 1])
                else:
                    V[i] = max(nums[first + 0], nums[first + 1])
            return max(V)

        n = len(nums)
        if n == 0: return 0
        return max(nums[0] + Rob1(2, n - 3), Rob1(1, n - 1))