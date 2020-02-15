

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    if n == 0: return ''
    maxL = 0
    maxPal = ''
    for i in range(n):
        for oddPal in [False, True]:
            if oddPal:
                # check the largest palindrome whose middle i
                first = i
                last = i
            else:
                # check the largest palindrome whose middle is between i,i+1
                first = i
                last = i + 1
            while (0 <= first) and (last <= n-1) and (s[first] == s[last]):
                L = last-first+1
                if L > maxL:
                    maxPal = s[first:last+1]
                    maxL = L
                first -= 1
                last += 1

    return maxPal

s = "a"
print(longestPalindrome(s))




# def isPal(s):
#     n = len(s)
#     if n == 0: return 0
#     if n % 2 == 0:
#         print(s[:(n // 2)], '==', s[n // 2:][::-1])
#         return s[:(n // 2)] == s[n // 2:][::-1]
#     else:
#         print(s[:((n // 2))], '==', s[n // 2 + 1:][::-1])
#         return s[:((n // 2))] == s[n // 2 + 1:][::-1]
#
#

# #
# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     n = len(s)
#     if n == 0: return ''
#     L = n # length
#     while (L>0):
#         print(L)
#         for i in range(n-L+1):
#             if isPal(s[i:i+L]):
#                 return s[i:i+L]
#         L -= 1
#     return ''

