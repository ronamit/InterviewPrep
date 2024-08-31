class Solution:
    def partitionString(self, s: str) -> int:
        if s == "":
            return 0
        ans = 1
        seen = set()
        for c in s:
            if c in seen:
                seen = set(c)
                ans += 1
            else:
                seen.add(c)
        return ans
