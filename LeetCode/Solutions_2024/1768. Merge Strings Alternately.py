class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        n1 = len(word1)
        n2 = len(word2)
        i1 = 0
        i2 = 0
        for i in range(n1 + n2):
            if i1 > n1 - 1:
                new_word += word2[i2]
                i2 += 1
            elif i2 > n2 - 1 or i % 2 == 0:
                new_word += word1[i1]
                i1 += 1
            else:
                new_word += word2[i2]
                i2 += 1
        return new_word
