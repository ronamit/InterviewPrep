from functools import lru_cache

"""
Note: a Trie data structure woule make it more efficent
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words_set = set(wordDict)
        word_lens = [len(w) for w in wordDict]
        max_word_len = max(word_lens)
        min_word_len = min(word_lens)

        @lru_cache(maxsize=None)
        def is_breakable(st: str) -> bool:
            nonlocal words_set, wordDict
            if st in words_set:
                return True
            for first_len in range(min_word_len, max_word_len + 1):
                if st[:first_len] in words_set and is_breakable(st[first_len:]):
                    return True

            return False

        return is_breakable(s)
