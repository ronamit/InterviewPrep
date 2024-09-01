from collections import Counter
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_counts = Counter(words)
        words_tuples = [(-count, word) for word, count in word_counts.items()]
        heapify(words_tuples)
        ans = []
        for _ in range(k):
            _, word = heappop(words_tuples)
            ans.append(word)
        return ans
