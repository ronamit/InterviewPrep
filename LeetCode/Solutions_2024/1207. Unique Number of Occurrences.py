from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cntr = Counter(arr)
        return len(cntr.values()) == len(set(cntr.values()))
