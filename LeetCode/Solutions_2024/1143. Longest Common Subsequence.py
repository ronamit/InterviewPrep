from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def longest_common(n1: int, n2: int) -> int:
            nonlocal text1, text2
            if n1 == 0 or n2 == 0:
                return 0
            if text1[n1 - 1] == text2[n2 - 1]:
                return 1 + longest_common(n1 - 1, n2 - 1)
            return max(longest_common(n1 - 1, n2), longest_common(n1, n2 - 1))

        n1 = len(text1)
        n2 = len(text2)
        return longest_common(n1, n2)
