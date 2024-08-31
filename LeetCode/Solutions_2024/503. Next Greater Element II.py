class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        #
        # use monotonic stack -
        # filled from right to left. throw away elements smaller than nums[i]
        #  we loop twice

        n = len(nums)
        nge = [-1 for _ in range(n)]
        stk = []
        for _ in range(2):
            for i in range(n - 1, -1, -1):
                while stk and stk[-1] <= nums[i]:
                    stk.pop()
                if stk:
                    nge[i] = stk[-1]
                stk.append(nums[i])
        return nge
