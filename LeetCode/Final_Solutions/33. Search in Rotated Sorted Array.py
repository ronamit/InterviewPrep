class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            if nums[0] == target:
                return  0
            else:
                return -1
        # first find pivot index by binary search
        def FindPivotInd(nums):
            low = 0
            high = n - 1
            while high >= low:
                if low == high:
                    return low
                mid = (low + high) // 2
                if nums[mid] < nums[mid - 1]:
                    return mid
                if nums[mid] < nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        pivot_ind = FindPivotInd(nums)
        # the conversion from index in non-rotated to the rotated:
        def ind_in_rot(i):
            return (pivot_ind + i) % n
        # now binary search with index adjusted according to pivot
        low = 0
        high = n - 1
        while high >= low:
            mid = (low + high) // 2
            mid_rot = ind_in_rot(mid)
            x = nums[mid_rot]
            if x == target:
                return mid_rot
            if x > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1







sol = Solution()
nums = [4,5,6,7,0,1,2]
target = 5
print(sol.search(nums, target))