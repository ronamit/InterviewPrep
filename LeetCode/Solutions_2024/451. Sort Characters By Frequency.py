from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = [(count, char) for char, count in Counter(s).items()]
        char_counts.sort(reverse=True)
        new_s = ""
        for count, char in char_counts:
            new_s += char * count
        return new_s
