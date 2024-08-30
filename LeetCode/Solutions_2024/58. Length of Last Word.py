class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words = [w for w in words if len(w) > 0 and w != " "]
        return len(words[-1])
