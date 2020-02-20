
from collections import deque

def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # this wil hold the last time we saw each character, when going back from end of s
    # (none if not seen yet)
    seen = {}
    for c in t:
        # for eah char in t: stack of the last seen indexes
        if c not in seen:
            seen[c] = deque([None])
        else:
            seen[c].append(None)
    n = len(s)
    minWinLen = n+ 1
    minWinLenStart = None
    maxDist = None
    for i in range(n - 1, -1, -1):
        c = s[i]
        if c not in seen.keys():
            # if not a char in t - skip
            continue
        seen[c].popleft()
        seen[c].append(i)
        # check if all chars of t has been seen (not None), and what is the maxDist:
        maxDist = None
        all_found = True
        for q in seen.values():
            if None in q:
                all_found = False
                break
            if maxDist is None:
                maxDist = q[0]
            else:
                maxDist = max(maxDist,q[0])

        if all_found:
            # if we saw all the chars in t
            # the minumum window len when start at i:
            winLen = maxDist - i + 1
            # print(s[i:i+winLen])
            if winLen < minWinLen:
                minWinLen = winLen
                minWinLenStart = i
    # print(minWinLen)
    if minWinLenStart is None:
        return ""
    else:
        return s[minWinLenStart:(minWinLenStart+minWinLen)]



self = None
# S = "ADOBECODEBANC"
# T = "ABC"
S = "aa"
T = "aa"
# S = "cabwefgewcwaefgcf"
# T = "cae"
print(minWindow(self, S, T))

#
# from collections import deque
#
# def minWindow(self, s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: str
#     """
#     # this wil hold the last time we saw each character, when going back from end of s
#     # (none if not seen yet)
#     seen = {}
#     for c in t:
#         # for eah char in t: stack of the last seen indexes
#         if c not in seen:
#             seen[c] = deque([None])
#         else:
#             seen[c].append(None)
#     n = len(s)
#     minWinLen = n+ 1
#     minWinLenStart = None
#
#     for i in range(n - 1, -1, -1):
#         c = s[i]
#         if c not in seen.keys():
#             # if not a char in t - skip
#             continue
#         seen[c].popleft()
#         seen[c].append(i)
#         # check if all chars of t has been seen (not None), and what is the maxDist:
#         maxDist = None
#         all_found = True
#         for q in seen.values():
#             if None in q:
#                 all_found = False
#                 break
#             if maxDist is None:
#                 maxDist = q[0]
#             else:
#                 maxDist = max(maxDist,q[0])
#
#         if all_found:
#             # if we saw all the chars in t
#             # the minumum window len when start at i:
#             winLen = maxDist - i + 1
#             # print(s[i:i+winLen])
#             if winLen < minWinLen:
#                 minWinLen = winLen
#                 minWinLenStart = i
#     # print(minWinLen)
#     if minWinLenStart is None:
#         return ""
#     else:
#         return s[minWinLenStart:(minWinLenStart+minWinLen)]
#
