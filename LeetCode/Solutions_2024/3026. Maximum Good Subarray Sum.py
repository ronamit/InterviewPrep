class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        ans = -float("inf")
        n = len(nums)
        cur_cum_sum = 0
        num_to_pre_sum = {}  # number in array; lowest cumulative sum until before an appearance of the num in nums array
        for i in range(n):
            x = nums[i]
            # save the pre-i cummalative sum if needed
            if x not in num_to_pre_sum:
                num_to_pre_sum[x] = cur_cum_sum
            else:
                num_to_pre_sum[x] = min(cur_cum_sum, num_to_pre_sum[x])
            # add the current number
            cur_cum_sum += x
            for sub_start in [x - k, x + k]:
                if sub_start in num_to_pre_sum:
                    # found good subarry
                    subarray_sum = cur_cum_sum - num_to_pre_sum[sub_start]
                    ans = max(ans, subarray_sum)
        return 0 if ans == -float("inf") else ans
