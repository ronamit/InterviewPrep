def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
     """
    cand_set = set(candidates)
    min_num = min(candidates)

    # TODO:  better solution
    def RecFunc(cand_set, target, min_num):
        if target == 0:
            return [] # empty set solution
        out = []
        if target in cand_set:
            out = [[target]]
        elif target < min_num:
            return [] # no solutions
        for a in candidates:
            if target - a >= min_num:
                sols = RecFunc(cand_set, target - a, min_num)
            else:
                sols = []
            for s in sols:
                out += [[a] + s]
        return out

    sols = RecFunc(cand_set, target, min_num)
    combs = set()
    for s in sols:
        s.sort()
        combs.add(tuple(s))
    combs = [list(cm) for cm in combs]
    return combs


self = None
candidates = [2,3,6,7]
target = 7
print(combinationSum(self, candidates, target))

#
# class Solution:
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#
#         candidates.sort()
#         candidates = candidates[::-1]
#
#     ==
#     n = len(candidates)
#     combs = []
#     for i in range(n):
#         a = candidates[i]
#         if a > target:
#             continue
#         if a == target:
#             combs += [target]
#     return combs
#
#
        #
        # cand_dic = {}
        # for a in candidates:
        #     if a in cand_dic:
        #         cand_dic[a] += 1
        #     else:
        #         cand_dic[a] = 1
        #
        # def RecFunc(cand_dic, target):
        #     if target == 0:
        #         return [[]]
        #     out = []
        #     for a in cand_dic.keys():
        #         target2 = target - a
        #         if target2 >= 0:
        #             out2 = RecFunc(cand_dic, target2)
        #             for s in out2:
        #                 out += [s+[a]]
        #     return out
        #
        # return RecFunc(cand_dic, target)
        #
        #
