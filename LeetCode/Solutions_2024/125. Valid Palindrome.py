class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        s = s.lower()
        n = len(s)
        if n % 2 == 0:
            a =  s[:(n//2)]
            b = s[(n//2):][::-1]
        else:
            a =  s[:((n-1)//2)]
            b = s[(((n-1)//2) + 1):][::-1]
        return a == b
