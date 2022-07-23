class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        n = len(digits)
        for i in range(n // 2):
            if digits[i] != digits[n-1-i]:
                return False
        return True

sol = Solution()
print(sol.isPalindrome(121))
