



# def wordBreak(self, s, wordDict):
#     """
#     :type s: str
#     :type wordDict: List[str]
#     :rtype: bool
#     """
#     wordSet = set(wordDict)
#     def RecFunc(start):
#         # run on the index of the char after break
#         L = len(s) - start
#         if L == 0:
#             return True
#         for i in range(start + 1, len(s) + 1):
#             prefix = s[start:i]
#             if prefix in wordSet:
#                 out = RecFunc(i)
#                 if out:
#                     return True
#         return False
#     return RecFunc(0)

    # TODO: non-recoursion

def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    wordSet = set(wordDict)
    n = len(s)
    if n == 0: return True
    good_inds = {0}
    for i in range(1, n+1):
        newInds = set()
        for j in good_inds:
                cand_s = s[j:i]
                if cand_s in wordSet:
                    newInds.add(i)
        good_inds = good_inds.union(newInds)
    return n in good_inds




self = None
# s = "leetcode"
# wordDict = ["leet", "code"]
s = "abcdefg"
wordDict = ["abcd", "efg"]
print(wordBreak(self, s, wordDict))



# def wordBreak(self, s, wordDict):
#     """
#     :type s: str
#     :type wordDict: List[str]
#     :rtype: bool
#     """
#     wordSet = set(wordDict)
#     def RecFunc(start):
#         # run on the index of the char after break
#         L = len(s) - start
#         if L == 0:
#             return True
#         for i in range(start + 1, len(s) + 1):
#             prefix = s[start:i]
#             if prefix in wordSet:
#                 out = RecFunc(i)
#                 return out
#         return False
#     return RecFunc(0)

