class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        x_neg = (x < 0)
        x = abs(x)
        while x != 0:
            y = y * 10 + x % 10
            x = x // 10
            if abs(y) > 2 ** 31:
                return 0
        if x_neg:
            y *= -1

        return y