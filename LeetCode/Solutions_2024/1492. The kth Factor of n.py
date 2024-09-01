class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i_factor = 0
        for i in range(1, n + 1):
            if n % i == 0:
                i_factor += 1
            if i_factor == k:
                return i
        return -1
