from collections import deque
import string


def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    # Do BFS
    q = deque([(beginWord, 1)])
    wordSet = set(wordList)
    while True:
        currWord, currDist = q.popleft()
        for i in range(len(currWord)+1):
            for c in string.ascii_lowercase:
                nextWord = currWord[:i]+c+currWord[i+1:]
                if nextWord in wordSet:
                    wordSet.remove(nextWord)
                    if nextWord == endWord:
                        return currDist+1
                    else:
                        q.append((nextWord, currDist+1))
        if not q:
            return 0 # empty stack - finish search
    return 0


self = None
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "a"
# endWord = "b"
# wordList = ["a","b","c"]
print( ladderLength(self, beginWord, endWord, wordList))





# from collections import deque
# ####
# # a more efficent solution - turn wordList in to a set , and to check neighbputs check all posiible one char changes, instead of going over the while list
# # https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
# ###
# def IsOneCharDiff(word1, word2):
#     n1 = len(word1)
#     n2 = len(word2)
#     if abs(n1 - n2) > 1:
#         return False
#     diffs = 0
#     for i in range(max(n1, n2)):
#         if i == n1 or i == n2 or word1[i] != word2[i]:
#             diffs += 1
#         if diffs == 2:
#             return False
#     return True
#
#
# def ladderLength(self, beginWord, endWord, wordList):
#     """
#     :type beginWord: str
#     :type endWord: str
#     :type wordList: List[str]
#     :rtype: int
#     """
#     # Do BFS
#     pathDist = [-1 for _ in wordList] # -1 == not visited
#     nWords = len(wordList)
#     currWord = beginWord
#     # if beginWord in wordList:
#     #     iword = wordList.index(beginWord)
#     #     pathDist[iword] = 0
#     probedDist = 1
#     q = deque()
#     while True:
#         for iword in range(nWords):
#             if pathDist[iword] > -1:
#                 continue
#             word = wordList[iword]
#             # check if currWord and word are different in only one letter
#             if IsOneCharDiff(word, currWord):
#                 pathDist[iword] = probedDist
#                 if word == endWord:
#                     return probedDist+1
#                 else:
#                     q.append(iword)
#         if not q:
#             return 0 # empty stack - finish search
#         icurrWord = q.popleft()
#         currWord = wordList[icurrWord]
#         probedDist = pathDist[icurrWord] + 1
#     return 0
#
#
# self = None
# # beginWord = "hit"
# # endWord = "cog"
# # wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "a"
# endWord = "b"
# wordList = ["a","b","c"]
# print( ladderLength(self, beginWord, endWord, wordList))