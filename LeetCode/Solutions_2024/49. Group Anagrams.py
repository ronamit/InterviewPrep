from collections import Counter
from string import ascii_lowercase


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = {}
        for i, s in enumerate(strs):
            counts = Counter(s)
            counts = tuple(counts.get(c, 0) for c in ascii_lowercase)
            anagrams_dict[counts] = [*anagrams_dict.get(counts, []), i]

        ans = []
        for word_inds in anagrams_dict.values():
            ans.append([strs[i] for i in word_inds])
        return ans
