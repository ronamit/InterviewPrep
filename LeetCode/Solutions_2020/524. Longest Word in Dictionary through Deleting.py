from typing import List, Dict, Tuple, Sequence
import itertools, collections


# auxiliary functions
def update_count(counter, c):
    if c not in counter.keys():
        counter[c] = 1
    else:
        counter[c] += 1

def get_index_in_s(c, last_used, chars):
    if c in last_used.keys():
        if last_used[c] >= len(chars[c]):
            return None
        index_from_s = chars[c][last_used[c]]
    else:
        index_from_s = chars[c][0]
    return index_from_s


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # pre-process s
        # create chars[c] = (indexes in s)
        chars = dict()
        for i, c in enumerate(s):
            if c not in chars.keys():
                chars[c] = ([i])
            else:
                chars[c].append(i)
            # endif
        # endfor
        # sort d
        d.sort(key=lambda w: (-len(w), w))
        # go over d
        for w in d:
            success = True
            last_used = dict() # last used index in chars[c] for each char that apeared so far in w
            i = 0  # we are allowed to use chars from s starting only from i
            for c in w:
                if c not in chars:
                    success = False
                    break  # w not good
                index_from_s = get_index_in_s(c, last_used, chars)
                while (index_from_s is not None) and (index_from_s < i):
                    update_count(last_used, c)
                    index_from_s = get_index_in_s(c, last_used, chars)
                if (index_from_s is None) or (index_from_s < i):
                    success = False
                    break  # w not good
                i = index_from_s + 1
                update_count(last_used, c)
            # endfor
            if success:
                return w
        # endfor
        return ''




s = "abpcplea"
d = ["ale","apple","monkey","plea"]

# s = "abpcplea"
# d = ["a","b","c"]

# s = "bab"
# d = ["ba","ab","a","b"]

sol = Solution()
print(sol.findLongestWord(s,d))