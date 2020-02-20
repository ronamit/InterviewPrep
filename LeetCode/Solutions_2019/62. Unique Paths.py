import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = math.factorial
        return f(m + n - 2) / (f(m - 1) * f(n - 1))
