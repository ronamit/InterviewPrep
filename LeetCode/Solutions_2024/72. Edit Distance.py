from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        @lru_cache(maxsize=None)
        def comp_T(k1, k2):
            if k2 == 0:
                ans = k1
            elif k1 == 0:
                ans = k2
            elif word1[k1-1] == word2[k2-1]:
                ans = comp_T(k1-1,k2-1)
            else:
                ans = min(1 + comp_T(k1-1,k2), 1 + comp_T(k1,k2-1),1 + comp_T(k1-1,k2-1))
            return ans
        return  comp_T(n1,n2)


