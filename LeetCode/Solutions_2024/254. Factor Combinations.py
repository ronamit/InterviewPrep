from functools import cache


class Solution:
    @cache  # noqa: B019
    def get_factors_tup(self, n: int) -> set[tuple[int]]:
        all_factors = set()
        for cand in range(2, n):
            if n % cand == 0:
                all_factors.add(tuple(sorted([cand, n // cand])))
                rest_possible_factors = self.get_factors_tup(n // cand)
                for rest_possiblity in rest_possible_factors:
                    all_factors.add(tuple(sorted([cand, *rest_possiblity])))
        return all_factors

    def getFactors(self, n: int) ->list[list[int]]:
        return [list(a) for a in self.get_factors_tup(n)]
