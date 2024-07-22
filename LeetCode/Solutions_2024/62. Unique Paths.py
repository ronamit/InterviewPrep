import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (n + m - 2) choose (m - 1)
        return math.comb(n + m - 2, m - 1)
