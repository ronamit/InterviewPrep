class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:

        n = len(values)
        left_max = [-float("inf") for _ in range(n)]
        left_max[0] = values[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], values[i] + i)
        ans = -float("inf")
        for j in range(1, n):
            ans = max(ans, left_max[j - 1] + values[j] - j)
        return ans
