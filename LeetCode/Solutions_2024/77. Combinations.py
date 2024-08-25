class Solution:
    def combine_aux(self, min_n: int, n: int, k: int) -> list[list[int]]:
        if k == 0:
            return [[]]  # empty sol
        if min_n > n or k > (n - min_n + 1):
            return [[]]
        combs = []
        for i in range(min_n, n + 1):
            rest_combs = self.combine_aux(min_n=i + 1, n=n, k=k - 1)
            for rest in rest_combs:
                combs.append([i, *rest])
        return combs

    def combine(self, n: int, k: int) -> list[list[int]]:
        combs = self.combine_aux(1, n, k)
        return [c for c in combs if len(c) == k]
