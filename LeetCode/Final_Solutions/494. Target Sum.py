

def add_dict(d, x, v):
    if x in d:
        d[x] += v
    else:
        d[x] = v

def dec_dict(d, x, v):
    d[x] -= v
    if d[x] == 0:
        del d[x]

class Solution:

    def findTargetSumWays(self, nums, S: int) -> int:

        n = len(nums)
        if n == 0: return S==0
        s_dict = {0: 1}
        for a in nums:
            s_dict_new = s_dict.copy()
            for x in s_dict:
                dec_dict(s_dict_new, x, s_dict[x])
                add_dict(s_dict_new, x+a, s_dict[x])
                add_dict(s_dict_new, x-a, s_dict[x])
            s_dict = s_dict_new
            print(s_dict)
            print(sum(s_dict.values()))
        print(s_dict)
        if S in s_dict:
            return s_dict[S]
        else:
            return 0



sol = Solution()
nums = [0,0,0,0,0,0,0,0,1]
S = 1
print(sol.findTargetSumWays(nums, S))

#
# class Solution:
#     def findTargetSumWays(self, nums, S: int) -> int:
#
#         n = len(nums)
#         if n == 0:
#             return S == 0
#         if nums[0] == 0:
#             return 2 * self.findTargetSumWays(nums[1:], S)
#         return self.findTargetSumWays(nums[1:], S - nums[0]) + self.findTargetSumWays(nums[1:], S + nums[0])
#
