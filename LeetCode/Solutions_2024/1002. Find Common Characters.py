from string import ascii_lowercase
import numpy as np
from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c_to_ind = {c: i for i, c in enumerate(ascii_lowercase)}
        cnt_per_word = np.zeros((len(words), len(ascii_lowercase)), dtype=int)
        for i_w, w in enumerate(words):
            for c, c_cnt in Counter(w).items():
                i_c = c_to_ind[c]
                cnt_per_word[i_w][i_c] = c_cnt
        min_cnt = cnt_per_word.min(axis=0)
        out_list = []
        for i, c in enumerate(ascii_lowercase):
            out_list += c * min_cnt[i]
        return list(out_list)
