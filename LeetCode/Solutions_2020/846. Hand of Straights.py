from typing import List, Dict, Tuple, Sequence
from  collections import OrderedDict

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        from collections import Counter
        counter = Counter(hand)  # count how many of each card
        # create list of [card, count], sorted by card
        cnt_hist = [[card, count] for card, count in sorted(counter.items(), key=lambda item: item[0])]
        n = len(cnt_hist)
        for i in range(n):
            card, count = cnt_hist[i]
            if count == 0:
                continue
            for shift in range(W):
                k = i + shift
                if k > n -1:
                    return False
                card_k, count_k = cnt_hist[k]
                if card_k != card + shift or count_k < count:
                    return False
                else:
                    cnt_hist[k][1] -= count
        return True


sol = Solution()

# print(sol.isNStraightHand(hand=[2,1], W=2))
print(sol.isNStraightHand(hand=[1,2,3,6,2,3,4,7,8], W=3))
