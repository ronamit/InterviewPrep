def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    slen = len(s)
    wordDict = set(wordDict)
    # saves the solutions for previous recursion calls:
    solvedFs = [None for _ in range(slen)]
    # Recursion function:
    def F(i):
        # F(i) = breaks for the string s[i:]
        # check if already solved F(i):
        if solvedFs[i] is not None:
            return solvedFs[i]
        breaks = []
        for j in range(i+1, slen+1):
            # check if the prefix of current string is in dict:
            w = s[i:j]
            if w in wordDict:
                if j == slen:
                    # found the final word:
                    breaks += [w]
                else:
                    # add the current word to all possible future breaks:
                    nextBreaks = F(j)
                    for b in nextBreaks:
                        breaks += [w + " " + b]
        solvedFs[i] = breaks
        return breaks
    return F(0)


self = None
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(self, s, wordDict))