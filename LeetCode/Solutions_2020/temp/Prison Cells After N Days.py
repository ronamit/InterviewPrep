# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/\\
from typing import List, Dict, Tuple, Sequence
import itertools, collections
import string
from copy import deepcopy


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        n_cells = len(cells)
        cells2 = [0 for i in range(n_cells)]
        for day in range(N):
            for i in range(1, n_cells - 1):
                if cells[i - 1] == cells[i + 1]:
                    cells2[i] = 1
                else:
                    cells2[i] = 0
                # end if
            # end for i
            is_change = False
            for i in range(n_cells):
                if cells2[i] != cells[i]:
                    cells[i] = cells2[i]
                    is_change = True
                # end if
            if not is_change:
                break
            print('day {}, cells = {}'.format(day, cells))
        # end for day
        return cells


# cells = [0,1,0,1,1,0,0,1]
# N = 7
cells = [1,0,0,1,0,0,1,0]
N = 50
print('cells=\n', cells)
print('N=\n', N)
sol = Solution()
print(sol.prisonAfterNDays(cells, N))