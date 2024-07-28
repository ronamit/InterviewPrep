class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans_set = set()
        n = len(nums)
        x_checked = set()
        for i in range(n):
            x = nums[i]
            if x in x_checked:
                continue
            x_checked.add(x)
            seen_nums = set()
            for j in range(i + 1, n):
                y = nums[j]
                z = -(x + y)
                if z in seen_nums:
                    inds = [x, y, z]
                    # print(x, y, z)
                    ans_set.add(tuple(sorted(inds)))
                seen_nums.add(y)
        ans_list = [list(inds) for inds in ans_set]
        return ans_list


# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         ans_set = set()
#         n = len(nums)
#         for i in range(n):
#             x = nums[i]
#             seen_nums = set()
#             for j in range(i + 1, n):
#                 y = nums[j]
#                 z = -(x + y)
#                 if z in seen_nums:
#                     inds = [x, y, z]
#                     print(x, y, z)
#                     ans_set.add(tuple(sorted(inds)))
#                 seen_nums.add(nums[j])
#             ans_list = [list(inds) for inds in ans_set]
#         return ans_list
