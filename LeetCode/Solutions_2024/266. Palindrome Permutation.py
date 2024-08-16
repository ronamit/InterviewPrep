from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        n_single = 0
        n_even = 0
        for c in cnt.values():
            if c == 1:
                n_single += 1
            elif c % 2 == 0:
                n_even += 1
        return n_even >= len(cnt) - 1
