class Solution:
    
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        return self.combinationSum2_aux(sorted(candidates), target)
    def combinationSum2_aux(self, candidates: list[int], target: int) -> list[list[int]]:
        if target < 0:
            return []
        if len(candidates) == 0:
            if target == 0:
                return [[]]
            return []
        ans = self.combinationSum2(candidates[1:], target)
        rest_ans = self.combinationSum2(candidates[1:], target - candidates[0])
        for comb in rest_ans:
            ans.append(sorted([candidates[0], *comb]))
        ans = [tuple(comb) for comb in ans]
        ans = set(ans)
        ans = [list(comb) for comb in ans]
        return ans


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
