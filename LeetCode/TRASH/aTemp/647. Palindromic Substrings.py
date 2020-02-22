# def isPal(s):
#     n = len(s)
#     if n == 0: return 0
#     if n % 2 == 0:
#         return s[:(n // 2)] == s[n // 2:][::-1]
#     else:
#         return s[:((n // 2))] == s[n // 2 + 1:][::-1]
#

#

class Solution:
    def countSubstrings(self, s: str):
        n = len(s)
        if isPal(s):
            return n + (n // 2)


            # for each char - find the last apearance
        # caeck if in between is a palindorme
        # then add the number of palindoemes contributed
        # and drop the char (continue)