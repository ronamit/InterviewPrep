from collections import Counter


# https://www.youtube.com/watch?v=wiGpQwVHdE0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1
        n = len(s)
        l = 0
        r = 0
        chars = set()  # the chars in the current substring
        while r < n:
            while s[r] in chars:
                if s[l] in chars:
                    chars.remove(s[l])
                l += 1
            max_len = max(max_len, r - l + 1)
            chars.add(s[r])
            r += 1
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
