class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True
        n_diffs = 0
        for i in range(n // 2):
            n_diffs += s[i] != s[n - 1 - i]
        return n_diffs <= 2
