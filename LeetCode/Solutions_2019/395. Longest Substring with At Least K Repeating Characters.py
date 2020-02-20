import collections
def longestSubstring(self, s: str, k: int):
    if s == '': return 0
    n = len(s)
    cnts1 = collections.Counter(s)
    min_reps = min(cnts1.values())
    max_len = 0
    for i in range(n):
        cnts2 = cnts1.copy()
        for j in range(n-1, i-1, -1):
            if min_reps >= k:
               max_len = max(j - i + 1, max_len)
               break
            c = s[j]
            cnts2[c] -= 1
            if cnts2[c] == 0:
                del cnts2[c]
                if not cnts2:
                    break
            min_reps = min(cnts2.values())
            max_reps = max(cnts2.values())
            if max_reps < k:
                break
        c = s[i]
        cnts1[c] -= 1
        if cnts1[c] == 0:
            del cnts1[c]
            if not cnts1:
                break
        min_reps = min(cnts1.values())
        max_reps = max(cnts1.values())
        if max_reps < k:
            break
    return max_len


self = None
s = "aacbbbdc"
k = 2
print(longestSubstring(self, s, k))

#
#
# def longestSubstring(self, s: str, k: int):
#     if s == '': return 0
#     countDict = {}
#     min_reps = len(s)
#     for c in s:
#         if not c in countDict:
#             countDict[c] = 1
#         else:
#             countDict[c] += 1
#     min_reps = min(countDict.values())
#
#     low = 0
#     high = len(s) - 1
#     while (high >= low):
#         if min_reps >= k:
#             print(s[low:high+1])
#             return high-low+1
#         ch = s[high]
#         cl = s[low]
#         cnt_h = countDict[ch]
#         cnt_l = countDict[cl]
#         if cnt_h < k:
#             high_down = True
#         elif cnt_l < k:
#             high_down = False
#         elif cnt_h < cnt_l:
#             high_down = True
#         else:
#             high_down = False
#         if high_down:
#             high -= 1
#             del_c = ch
#         else:
#             low += 1
#             del_c = ch = cl
#
#         countDict[del_c] -= 1
#         if countDict[del_c] == 0:
#             del countDict[del_c]
#             if not countDict:
#                 return 0
#         min_reps = min(countDict.values())
#
#     return 0
#
