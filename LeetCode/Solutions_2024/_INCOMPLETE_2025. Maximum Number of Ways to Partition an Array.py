def add_to_seen(d, x, i):
    if x not in d:
        d[x] = [i]
    else:
        d[x] += [i]


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:

        n = len(nums)
        optimal_sols = set() # set of pivot: replaced index (used to avoid duplicates)

        # cummaltive sum
        up_sum = [None for _ in range(n)]
        for i in range(n):
            if i == 0:
                up_sum[i] = nums[i]
            else:
                up_sum[i] = nums[i] + up_sum[i - 1]
        down_sum = [None for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                down_sum[i] = nums[i]
            else:
                down_sum[i] = nums[i] + down_sum[i + 1]

        # go up the indexes and see if we get up_sum[i] == down_sum[i] for some i
        # or if we can fix the diff with a k replacement from 0..i
        seen_nums = {nums[0]: [0]}  #  x : seem indexes
        for pivot in range(1, n):
            diff =  down_sum[pivot]-  up_sum[pivot - 1]
            if diff == 0:
                optimal_sols.add((pivot, None))
                
            if diff != 0 and (k - diff) in seen_nums:
                for i in seen_nums[k - diff]:
                    optimal_sols.add((pivot, i))
            add_to_seen(seen_nums, nums[pivot], pivot)

        # go down the indexes and see if for some i
        # or if we can fix the diff with a k replacment from i,..,n-1
        seen_nums = {}  #   x : count seen
        for pivot in range(n - 1, 0, -1):  # n-1,...,1
            diff = up_sum[pivot]  = down_sum[pivot - 1]
            if diff != 0 and  (k - diff) in seen_nums:
                for i in seen_nums[k - diff]:
                    optimal_sols.add((pivot, i))
            add_to_seen(seen_nums, nums[pivot], pivot)

        print(optimal_sols)
        return len(optimal_sols)

sol = Solution()
# nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30827,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
k = 0
print(sol.waysToPartition(nums, k))