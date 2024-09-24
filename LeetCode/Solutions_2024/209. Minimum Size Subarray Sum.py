from collections import deque


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        min_len = float("inf")
        queue = deque()
        q_sum = 0
        for i in range(n):
            queue.append(nums[i])
            q_sum += nums[i]
            while queue and q_sum >= target:
                min_len = min(min_len, len(queue))
                x = queue.popleft()
                q_sum -= x

        return 0 if min_len == float("inf") else min_len
