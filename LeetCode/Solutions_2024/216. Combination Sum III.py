from functools import cache


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        # for each 1,..,9 we decide to include or not
        # A[min_num, k, n] = list of k-numbers lists in  min_num,...,9  that sum to n

        @cache
        def find_comb(min_num: int, k: int, n: int) -> list[list[int]]:
            if k <= 0 and n > 0:
                return []
            if k == 0 and n == 0:
                return [[]]
            if min_num > 9:
                return []
            if n < min_num:
                return []
            # two cases: either min_num is in the combination or not
            rest_comb1 = find_comb(min_num + 1, k - 1, n - min_num)
            combs1 = [[min_num, *rest_nums] for rest_nums in rest_comb1]
            combs2 = find_comb(min_num + 1, k, n)
            return combs1 + combs2

        return find_comb(1, k, n)
