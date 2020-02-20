class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        def IsSub(s, t):
            n = len(t)
            if len(s) == 0:
                return True
            if n == 0:
                return False
            for j in range(n):
                if t[j] == s[0] and IsSub(s[1:], t[j + 1:]):
                    return True
            return False

        return IsSub(s, t)