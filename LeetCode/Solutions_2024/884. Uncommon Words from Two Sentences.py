from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        ans = []
        for w, cnt1 in c1.items():
            if cnt1 == 1 and w not in c2:
                ans.append(w)

        for w, cnt2 in c2.items():
            if cnt2 == 1 and w not in c1:
                ans.append(w)
        return ans
