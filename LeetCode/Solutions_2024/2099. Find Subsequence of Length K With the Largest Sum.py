import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        nums_and_inds = [(nums[i], i) for i in range(n)]
        # find the k largest elements
        h = heapq.nlargest(k, nums_and_inds, key=lambda x: x[0])
        # sort the k largest elements by their indices
        h.sort(key=lambda x: x[1])
        # return the k largest elements
        return [x[0] for x in h]


sol = Solution()
print(sol.maxSubsequence([2, 1, 3, 3], 2))
