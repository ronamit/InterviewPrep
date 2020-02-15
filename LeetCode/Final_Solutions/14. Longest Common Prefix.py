def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs is None:
        return ''
    n = len(strs)
    if n==0:
        return ''
    minlen = min([len(s) for s in strs])
    if minlen == 0:
        return ''
    go = True
    pos = 0
    while go and pos < minlen:
        for i in range(1, n):
            if strs[0][pos] != strs[i][pos]:
                go = False
                break
        if go:
            pos += 1
    return strs[0][:pos]






self=None
# in_strs = ["flower","flow","flight"]
in_strs = ['C', 'C']
print(longestCommonPrefix(self, in_strs))

#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         i = 0
#         goOn = True
#         while goOn:
#             for s in strs:
#                 if len(s) - 1 < i or strs[0][i] != s[i]:
#                     goOn = False
#                     break
#             i += 1
#         return strs[0][:i - 1]
#
