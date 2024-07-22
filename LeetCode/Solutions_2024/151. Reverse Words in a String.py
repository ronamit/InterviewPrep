class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        words = [w for w in words if w != ""]
        s_new = ""
        for w in words[::-1]:
            s_new += w.strip() + " "
        s_new = s_new[:-1]
        return s_new

sol = Solution()
print(sol.reverseWords("example   good a"))