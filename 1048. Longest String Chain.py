
from typing import List, Dict, Tuple, Sequence
import string

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        n = len(words)

        # sort by word len in ascending order (- does topological ordering)
        words.sort(key=lambda w: len(w))


        # create word->index dict
        d = dict()
        for i, w in enumerate(words):
            d[w] = i

        # create adjacency list
        possible_chars = [c for c in string.ascii_lowercase if c != '']
        edges_out = [set() for i in range(n)]     # edges_in[u] == v means edge (u,v)
        for i, w in enumerate(words):
            L = len(w)
            for k in range(L+1):  # k == insertion index
                for c in possible_chars:
                    w2 = w[:k] + c + w[k:]
                    if w2 in d.keys():
                        j = d[w2]
                        if j not in edges_out[i]:
                            edges_out[i].add(j)

        # Use dynamic-prog to find max len
        max_starts_in_ind = [1 for i in range(n)] # max chain that starts in each index
        for i in range(n-2, -1, -1):
            max_curr = 1
            for j in edges_out[i]:
                max_curr = max(max_curr, 1 + max_starts_in_ind[j])
            max_starts_in_ind[i] = max_curr

        max_chain_len = max(max_starts_in_ind)

        # # debug
        # edges = []
        # for i, outs in enumerate(edges_out):
        #     for j in outs:
        #         edges.append((i,j))
        # print(edges)


        return max_chain_len

#----------------------------------------------------------#

sol = Solution()
# words = ["a","b","ba","bca","bda","bdca"]
words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
print(sol.longestStrChain(words))