"""
    See a good soluition here: https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/solutions/1507271/python-cpp-explanation-with-pictures-o-n/?envType=company&envId=google&favoriteSlug=google-thirty-days
"""

import itertools


def add_to_seen(d, x, i):
    if x not in d:
        d[x] = [i]
    else:
        d[x] += [i]


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:

        n = len(nums)
        sol_without_replace = 0
        sol_with_replace = [0 for _ in range(n)]  # for each index, how many solutions are optimal if we change it

        # cummaltive sum
        up_sum = list(itertools.accumulate(nums))
        down_sum = list(itertools.accumulate(nums[::-1]))[::-1]

        # go up the indexes with i and see if we get up_sum[i] == down_sum[i]
        # or if we can fix the diff with a k replacement of an item from 0..i
        seen_nums = {}  #  x : seem indexes
        add_to_seen(seen_nums, nums[0], 0)
        for pivot in range(1, n):
            add_to_seen(seen_nums, nums[pivot], pivot)
            diff = down_sum[pivot] - up_sum[pivot - 1]
            if diff == 0:
                sol_without_replace += 1
            else:
                replace_candidate = k - diff  # the value we need to replace to make the sums equal
                if replace_candidate in seen_nums:
                    for i in seen_nums[replace_candidate]:
                        sol_with_replace[i] += 1

        # go down the indexes with i and see if we can fix the diff with a k replacement of an item in i,..,n-1
        seen_nums = {}  #   x : count seen
        for pivot in range(n - 1, 0, -1):  # n-1,...,1
            add_to_seen(seen_nums, nums[pivot], pivot)
            diff = up_sum[pivot] - down_sum[pivot - 1]
            if diff == 0:
                # this case was covered above
                pass
            else:
                replace_candidate = k - diff  # the value we need to replace to make the sums equal
                if replace_candidate in seen_nums:
                    for i in seen_nums[replace_candidate]:
                        sol_with_replace[i] += 1

        ans = max(sol_without_replace, *sol_with_replace)
        print(f"sol_with_replace = {sol_with_replace}")
        print
        return ans


sol = Solution()
# nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0
print(sol.waysToPartition(nums, k))
