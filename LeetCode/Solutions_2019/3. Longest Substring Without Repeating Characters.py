def lengthOfLongestSubstring(self, s: 'str') -> 'int':
    last_seen = {}
    n = len(s)
    if n == 0:
        return 0
    maxlen = 0
    prevlen = 0
    for i in range(n):
        c = s[i]
        if c not in last_seen:
            c_last_seen = -1
        else:
            c_last_seen = last_seen[c]
        if (c_last_seen == -1):
            curlen = prevlen + 1
        else:
            curlen = min(prevlen + 1, i - c_last_seen)
        prevlen = curlen
        maxlen = max(maxlen, curlen)
        last_seen[c] = i
    return maxlen


self = None
s = "abcabcbb"
print(lengthOfLongestSubstring(self, s))


#
#
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         if n == 0: return 0
#         a = [1 for i in range(n)]
#         max_a = 1
#         i_max = 0
#         for i in range(1, n, +1):
#             j = i-1
#             for j in range(i-1, i-1-a[i-1],-1):
#                 if s[i] == s[j]:
#                     j += 1
#                     break
#             a[i] =  i - j + 1
#             if a[i] > max_a:
#                 i_max = i
#                 max_a = a[i]
#         return max_a