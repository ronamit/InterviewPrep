class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        prefix_sums = [nums[0]]
        for i in range(1, n):
            prefix_sums.append(nums[i] + prefix_sums[-1])
        max_len = 0
        prev_sums = {0: -1}  # sum: leftmost index it was seen
        for i in range(n):
            cur_sum = prefix_sums[i]
            if (cur_sum - k) in prev_sums:
                max_len = max(max_len, i - prev_sums[cur_sum - k])
            if cur_sum not in prev_sums:
                prev_sums[cur_sum] = i
        return max_len
